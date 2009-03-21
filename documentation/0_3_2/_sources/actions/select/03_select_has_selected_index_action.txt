===========================================
I see "some" select has selected index of 1
===========================================

Syntax
------
::

	I see "<select name>" select has selected index of <index>

where:
	``<select name>`` - name or id for the desired select element
	
	``<index>`` - index to check against
	
Description
-----------
Asserts that the specified select has the specified index as currently selected index.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.


Raises
------
Raises ActionFailedError if the select has any select index other than the specified.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "selSomething" select has selected index of 1
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Select Has Selected Index action.