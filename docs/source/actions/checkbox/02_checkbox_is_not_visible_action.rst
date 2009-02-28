============================
I do not see "some" checkbox
============================

Syntax
------
::

	I do not see "<checkbox name>" checkbox

where:
	``<checkbox name>`` - name or id for the desired input type="checkbox"
	
Description
-----------
Asserts that the specified checkbox does not exist or is invisible.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

.. note::

   Invisible here means style="display:none" or style="visibility:hidden".

Raises
------
Raises ActionFailedError if the checkbox exists **AND** is visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I do not see "chkSomething" checkbox
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.2
   Checkbox Is Not Visible action.