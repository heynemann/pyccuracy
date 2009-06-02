======================
I clean "some" textbox
======================

Syntax
------
::

	I clean "<textbox name>" textbox

where:
	``<textbox name>`` - name or id for the desired input type="text" or textarea.
	
Description
-----------
Cleans the specified textbox's or textarea's text.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   	
Examples
--------
::

	...
	When
		I clean "txtQuery" textbox
	...
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4
   Textbox Clean action.
