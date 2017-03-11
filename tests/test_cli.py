"""Unit tests for pynlpir's cli.py file."""
import os
import shutil
import stat
import unittest
try:
    from urllib.error import URLError
    from urllib.request import urlopen
except ImportError:
    from urllib2 import URLError, urlopen

from click.testing import CliRunner

from pynlpir import cli

TEST_DIR = os.path.abspath(os.path.dirname(__file__))
LICENSE_FILE = os.path.join(TEST_DIR, 'data', 'NLPIR.user')


def can_reach_github():
    """Check if we can reach GitHub's website."""
    try:
        urlopen('http://github.com')
        return True
    except URLError:
        return False


@unittest.skipIf(can_reach_github() is False, 'Unable to reach GitHub')
class TestCLI(unittest.TestCase):
    """Unit tests for the PyNLPIR CLI."""

    def setUp(self):
        self.runner = CliRunner()

    def tearDown(self):
        self.runner = None

    def test_initial_license_download(self):
        """Tests that an initial license download works correctly."""
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(cli.cli, ('update', '-d.'))
            self.assertEqual(0, result.exit_code)
            self.assertEqual('License updated.\n', result.output)

    def test_license_update(self):
        "Test that a regular license update works correctly."""
        with self.runner.isolated_filesystem():
            shutil.copyfile(LICENSE_FILE, os.path.basename(LICENSE_FILE))

            result = self.runner.invoke(cli.cli, ('update', '-d.'))
            self.assertEqual(0, result.exit_code)
            self.assertEqual('License updated.\n', result.output)

            result = self.runner.invoke(cli.cli, ('update', '-d.'))
            self.assertEqual(0, result.exit_code)
            self.assertEqual('Your license is already up-to-date.\n',
                             result.output)

    def test_license_write_fail(self):
        """Test tha writing a license file fails appropriately."""
        with self.runner.isolated_filesystem():
            cwd = os.getcwd()
            os.chmod(cwd, stat.S_IREAD)
            with self.assertRaises((IOError, OSError)):
                cli.update_license_file(cwd)
