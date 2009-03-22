==============================================================
I see "some" select does not have selected text of "something"
==============================================================

Syntax
------
::

	I see "<select name>" select does not have selected text of "<text>"

where:
	``<select name>`` - name or id for the desired select element
	
	``<text>`` - text to check against
	
Description
-----------
Asserts that the specified select does not have the specified text as the currently selected option's text.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the select has the specified text as the selected option's text.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "selSomething" select does not have selected text of "Holy Graal"
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4
   Select Does Not Have Selected Text action.
