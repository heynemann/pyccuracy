=================
Pyccuracy Console
=================

Introduction
------------

The pyccuracy console app is provided as means of executing pyccuracy files (.acc).

It is just a regular python app (pyccuracy_console.py) and thus can be run like other python apps.

The only difference is that it takes command-line arguments in the form of::

    pyccuracy_console.py [option]
    
If no options are specified it gets executed with the defaults and runs all the tests in the given folder (you can learn more about the defaults in each of the accepted arguments).

The options can be specified in two forms::

    -<short_option_name> <value>
    
Or::

    --<long_option_name>=<value>

Both forms specify exactly the same configuration. Choose the one you're more comfortable with.

Arguments
---------

-d or --dir
===========

Description
'''''''''''

This is the tests root directory. 

Defines where the tests to be executed are. 

.. note::

   The test execution is recursive, so all the tests under the specified directory (even in sub-directories) get executed.

Default
'''''''

Defaults to the current shell directory.

Example
'''''''

::

    pyccuracy_console.py -d /path/to/tests
    pyccuracy_console.py --dir=/path/to/tests
    
-p or --pattern
===============

Description
'''''''''''

Test File naming pattern. 

Defines which tests will get executed.

.. note::

   This parameter can use wildcards supported by the OS.

Default
'''''''

Defaults to "*.acc".

Example
'''''''

::

    pyccuracy_console.py -p some_test.acc
    pyccuracy_console.py --pattern=some_test.acc

*This will only execute the some_test.acc test.*

-u or --url
===========

Description
'''''''''''

This is the website being tested base URL. 

When the user navigates to a given page that page will be joined with this url.

.. note::

   This parameter can be specified with a physical url (/some/path/to/pages) or a web url (http://www.google.com).

Default
'''''''

Defaults to None.

Example
'''''''

::

    pyccuracy_console.py -u http://www.mysite.com
    pyccuracy_console.py --url=http://www.mysite.com
    
This means that if some user navigates to "some_page.htm" Pyccuracy will actually navigate to "http://www.mysite.com/some_page.htm".
