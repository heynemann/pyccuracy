===========================================
I see "some" select has selected value of 1
===========================================

Syntax
------
::

	I see "<select name>" select has selected value of <index>

where:
	``<select name>`` - name or id for the desired select element
	
	``<value>`` - value to check against
	
Description
-----------
Asserts that the specified select has the specified value as currently selected value.

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
		I see "selSelectedValue" select has selected value of 1
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.3
   Select Has Selected Value action.
