========
Tutorial
========

Installing
----------

Assuming you have easy_install installed, all you need to do is::

    easy_install pyccuracy (or sudo easy_install pyccuracy in unix)

Creating your .acc tests
------------------------

Even though you can create tests using any extension you'd like and any file format
(since Pyccuracy let's you override), you're better off using the defaults.

Just name your files with the .acc extension and name your tests whatever you want, so for example::

    see_that_google_works.acc

Running the tests
-----------------

First, import Pyccuracy, using::

    from pyccuracy.pyccuracy_core import *

Then create an instance of Pyccuracy using::

    pyccuracy = Pyccuracy()

The easiest form is::
    
    pyccuracy.run_tests()

This means running all test files with the .acc extension in the same folder as the test being run,
using en-us language (default).

If you need to specify the path to your tests, use::

    pyccuracy.run_tests(tests_path = "/path/to/tests")

For a specific language, use::

    pyccuracy.run_tests(default_culture = "pt-br")

This runs all the tests using Portuguese Brazil language.

The other options in the run_tests method will be explained in later releases.

Reading the results
-------------------

To be written.

Custom actions
--------------

To be written.