=====================
I see "some" checkbox
=====================

Syntax
------
::

	I see "<checkbox name>" checkbox

where:
	``<checkbox name>`` - name or id for the desired input type="checkbox"
	
Description
-----------
Asserts that the specified checkbox exists **AND** is visible.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the checkbox does not exist or is not visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "chkSomething" checkbox
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Checkbox Is Visible action.