======================================================
I select the option with value of "1" in "some" select 
======================================================

Syntax
------
::

	I select the option with value of "<value>" in "<select name>" select 

where:
	``<value>`` - value to select
	
	``<select name>`` - name or id for the desired select element
	
Description
-----------
Changes the selected value in the given select to the specified value.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
	
Examples
--------
::

	...
	When
		I select the option with value of "2" in "selSomething" select 
	Then
		I see "selSomething" select has selected value of "2"
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4
   Select Option By Value action.
