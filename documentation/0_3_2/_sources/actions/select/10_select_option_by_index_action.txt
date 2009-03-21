====================================================
I select the option with index of 1 in "some" select 
====================================================

Syntax
------
::

	I select the option with index of <index> in "<select name>" select 

where:
	``<index>`` - index to select
	
	``<select name>`` - name or id for the desired select element
	
Description
-----------
Changes the selected index in the given select to the specified index.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
	
Examples
--------
::

	...
	When
		I select the option with index of 2 in "selSomething" select 
	Then
		I see "selSomething" select has selected index of 2
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Select Option By Index action.