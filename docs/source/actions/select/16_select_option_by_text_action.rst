=============================================================
I select the option with text of "something" in "some" select 
=============================================================

Syntax
------
::

	I select the option with text of "<text>" in "<select name>" select 

where:
	``<text>`` - text of the option to select
	
	``<select name>`` - name or id for the desired select element
	
Description
-----------
Changes the selected option in the given select to the to the one with the specified text.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
	
Examples
--------
::

	...
	When
		I select the option with text of "Holy Graal" in "selSomething" select 
	Then
		I see "selSomething" select has selected text of "Holy Graal"
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4
   Select Option By Text action.
