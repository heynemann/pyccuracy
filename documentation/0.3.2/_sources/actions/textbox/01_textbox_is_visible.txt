====================
I see "some" textbox
====================

Syntax
------
::

	I see "<textbox name>" textbox

where:
	``<textbox name>`` - name or id for the desired textbox element
	
Description
-----------
Asserts that the specified textbox exists **AND** is visible.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.


Raises
------
Raises ActionFailedError if the textbox does not exist or is not visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "txtSomething" textbox
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.2
   Textbox Is Visible action.