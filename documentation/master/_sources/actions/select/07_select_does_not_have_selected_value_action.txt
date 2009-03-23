=======================================================
I see "some" select does not have selected value of "1"
=======================================================

Syntax
------
::

	I see "<select name>" select does not have selected value of "<value>"

where:
	``<select name>`` - name or id for the desired select element
	
	``<value>`` - value to check against
	
Description
-----------
Asserts that the specified select does not have the specified value as the currently selected option's value.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

.. warning::

   The delimiters around the value are needed since in HTML values can be strings.

Raises
------
Raises ActionFailedError if the select has the specified value as the selected option's value.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "selSomething" select does not have selected value of "1"
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4
   Select Does Not Have Selected Value action.
