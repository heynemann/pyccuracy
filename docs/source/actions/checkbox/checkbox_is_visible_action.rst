=====================
I see "some" checkbox
=====================

Syntax
------
::

	I see "<checkbox name>" checkbox

where:
	<checkbox name> - name for the desired input type="checkbox"
	
Description
-----------
Asserts that the specified checkbox exists **AND** is visible.

Raises
------
Raises ActionFailedError if the checkbox does not exist or is not visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Example
-------
::

	...
	Then
		I see "chkSomething" checkbox
	
*Rest of the test ommitted for clarity*

.. versionadded:: 0.1
   Checkbox Is Visible action.