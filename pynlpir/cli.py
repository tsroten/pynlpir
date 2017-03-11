"""The command-line interface to PyNLPIR."""

import hashlib
import os
import shutil
import tempfile
try:
    from urllib.error import URLError
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve
    from urllib2 import URLError

import click

import pynlpir

LICENSE_URL = ('https://github.com/NLPIR-team/NLPIR/raw/master/License/license'
               '%20for%20a%20month/NLPIR-ICTCLAS%E5%88%86%E8%AF%8D%E7%B3%BB%E7'
               '%BB%9F%E6%8E%88%E6%9D%83/NLPIR.user')
DATA_DIR = os.path.join(pynlpir.nlpir.PACKAGE_DIR, 'Data')
LICENSE_FILENAME = 'NLPIR.user'


@click.group(context_settings=dict(help_option_names=['-h', '--help']),
             options_metavar='[<options>]',
             subcommand_metavar='<command> [<args>]')
@click.version_option(pynlpir.__version__, message='%(prog)s %(version)s')
def cli():
    """A simple command-line interface for PyNLPIR."""
    pass


def update_license_file(data_dir):
    """Update NLPIR license file if it is out-of-date or missing.

    :param str data_dir: The NLPIR data directory that houses the license.
    :returns bool: Whether or not an update occurred.

    """
    license_file = os.path.join(data_dir, LICENSE_FILENAME)
    temp_dir = tempfile.mkdtemp()
    gh_license_filename = os.path.join(temp_dir, LICENSE_FILENAME)
    try:
        _, headers = urlretrieve(LICENSE_URL, gh_license_filename)
    except IOError as e:
        # Python 2 uses the unhelpful IOError for this. Re-raise as the more
        # appropriate URLError.
        raise URLError(e.strerror)

    with open(gh_license_filename, 'rb') as f:
        github_license = f.read()

    try:
        with open(license_file, 'rb') as f:
            current_license = f.read()
    except (IOError, OSError):
        current_license = b''

    github_digest = hashlib.sha256(github_license).hexdigest()
    current_digest = hashlib.sha256(current_license).hexdigest()

    if github_digest == current_digest:
        return False

    shutil.copyfile(gh_license_filename, license_file)
    shutil.rmtree(temp_dir, ignore_errors=True)
    return True


@cli.command(options_metavar='<options>')
@click.option('-d', '--data-dir', help='The NLPIR data directory to use.',
              type=click.Path(exists=True, file_okay=False, writable=True),
              default=DATA_DIR)
def update(data_dir):
    """Update NLPIR license."""
    try:
        license_updated = update_license_file(data_dir)
    except URLError:
        click.secho('Error: unable to fetch newest license.', fg='red')
        exit(1)
    except (IOError, OSError):
        click.secho('Error: unable to move license to data directory.',
                    fg='red')
        exit(1)

    if license_updated:
        click.echo('License updated.')
    else:
        click.echo('Your license is already up-to-date.')


if __name__ == '__main__':
    cli()
