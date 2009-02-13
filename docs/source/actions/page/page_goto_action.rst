==================
I go to "some url"
==================

Syntax
------
::

	I go to "<url>"

where:
	``<url>`` - url to navigate to.
		
Description
-----------
Navigate the browser to the specified url.

.. note::

   The ``url`` parameter can take an url in the form of "http://www.google.com" or a path.
   
   If a path is used it will be joined with the directory specified by ``root_dir`` when Pyccuracy was called. 
   This usually means the folder where the tests are being run.
   	
Examples
--------
1) Navigate to http://www.google.com
::

	Given
		I go to "http://www.google.com"
	When
		...
	
2) Navigate to my_shiny_page.htm in the current folder.
::

	Given
		I go to "my_shiny_page.htm"
	When
		...
		
What happens is that, since we are running from c:\\my\\special\\path (windows) and 
Pyccuracy gets a value that's not an url (``I go to "my_shiny_page.htm"``), 
it will navigate to ``file://c:/my/special/path/my_shiny_page.htm``.

		
*Rest of the tests ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Page Go To action.