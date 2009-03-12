====================================================
I see "some" select has selected text of "Something"
====================================================

Syntax
------
::

	I see "<select name>" select has selected text of "<text>"

where:
	``<select name>`` - name or id for the desired select element
	
	``<text>`` - text to check against
	
Description
-----------
Asserts that the specified select has the specified text as currently selected item's text.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the select has a select value other than the specified.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "selSelectedText" select has selected text of "Shrubbery"
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.3
   Select Has Selected Text Action.
