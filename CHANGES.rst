.. :changelog:

Change Log
----------

0.4.5 (2016-07-18)
++++++++++++++++++

* Updates NLPIR license.

0.4.4 (2016-04-09)
++++++++++++++++++

* Updates NLPIR license.

0.4.3 (2016-03-13)
++++++++++++++++++

* Updates NLPIR license.

0.4.2 (2016-02-16)
++++++++++++++++++

* Updates NLPIR license.

0.4.1 (2016-01-22)
++++++++++++++++++

* Updates NLPIR license.

0.4 (2015-12-21)
++++++++++++++++

* Updates NLPIR.
* Adds OS X support.

0.3.3 (2015-10-21)
++++++++++++++++++

* Fixes NLPIR freezing with certain inputs. Fixes #33.
* Adds flake8 tests to tox and travis-ci.
* Adds tests for Python 3.5 support.
* Uses io.open() in setup.py. Fixes #34.


0.3.2 (2015-08-05)
++++++++++++++++++

* Adds 2015-08-05 license file. Fixes #31.

0.3.1 (2015-07-12)
++++++++++++++++++

* Fixes RST rendering error.

0.3 (2015-07-12)
++++++++++++++++

* Includes NLPIR version 20150702. Fixes #25.
* Adds encoding error handling scheme options.
* Adds new word identification functions and documentation. Fixes #26.
* Makes ``~pynlpir.get_key_words`` work with multiple NLPIR return value
  structures. Fixes #23.
* Returns ``None`` when pos code not recognized. Fixes #20.
* Updates outdated link in tutorial. Fixes #21.

0.2.2 (2015-01-02)
++++++++++++++++++

* Fixes release problem with v0.2.1.

0.2.1 (2015-01-02)
++++++++++++++++++

* Packages NLPIR version 20141230. Fixes #18.

0.2 (2014-12-18)
++++++++++++++++

* Packages NLPIR version 20140926. Restores ``pynlpir.get_key_words`` functionality. Fixes #11, #14, and #15.
* Updates part of speech map for new NLPIR version. Fixes #17.
* Fixes a typo in ``api.rst``. Fixes #16.
* Fixes a bug involving uppercase part of speech codes. Fixes #10.
* Adds Python 3.4 test to tox and travis.
* Notes Python 3.4 support in ``setup.py`` and ``CONTRIBUTING.rst``.
* Fixes the doubleslash unit test so that it works with the new NLPIR version.
* Adds a missing comma. Fixes #8.
* Fixes indentation in ``pynlpir.get_key_words``.
* Adds condition for empty key word result. Fixes #9.

0.1.3 (2014-06-12)
++++++++++++++++++

* Fixes typo in docs. Fixes #4.
* Adds *license_code* argument to ``pynlpir.open``. Fixes #6.
* Packages NLPIR version 20131219 and removes version 20140324. Fixes a NLPIR expired license issue. Fixes #5.
* Fixes bug with double slashes in input. Fixes #7.

0.1.2 (2014-05-01)
++++++++++++++++++

* Adds version information to ``__init__.py``.
* Adds Travis CI configuration information.
* Reformats ``README.rst``.
* Adds documentation about contributing.
* Fixes #2. Fixes segmenting text with whitespace.
* Fixes #3. Fixes ``_encode()``/``_decode`` default encoding error.

0.1.1 (2014-04-07)
++++++++++++++++++

* Fixes installation problem with package data.

0.1.0 (2014-04-07)
++++++++++++++++++

* Initial release.
