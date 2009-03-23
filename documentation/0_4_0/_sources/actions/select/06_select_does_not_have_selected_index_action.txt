=====================================================
I see "some" select does not have selected index of 1
=====================================================

Syntax
------
::

	I see "<select name>" select does not have selected index of <index>

where:
	``<select name>`` - name or id for the desired select element
	
	``<index>`` - index to check against
	
Description
-----------
Asserts that the specified select does not have the specified index as currently selected index.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.


Raises
------
Raises ActionFailedError if the select has the specified index as the selected option's index.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "selSomething" select does not have selected index of 1
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4
   Select Does Not Have Selected Index action.
