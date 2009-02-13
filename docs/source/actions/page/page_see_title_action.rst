==================
I see "some" title
==================

Syntax
------
::

	I see "<title>" title

where:
	``<title>`` - title for the document currently loaded in the web browser
	
Description
-----------
Asserts that the currently loaded document in the web browser has the specified title.
	
Raises
------
Raises ActionFailedError if the current document's title is not the specified.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "Hello World - Google Search" title

*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Page See Title action.