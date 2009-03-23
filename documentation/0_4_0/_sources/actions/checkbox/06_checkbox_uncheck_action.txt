=============================
I uncheck the "some" checkbox
=============================

Syntax
------
::

	I uncheck the "<checkbox name>" checkbox

where:
	``<checkbox name>`` - name or id for the desired input type="checkbox"
	
Description
-----------
Marks the given checkbox as not checked.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the checkbox is not visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	When
		I uncheck the "chkSomething" checkbox
	Then
		I see the "chkSomething" checkbox is not checked
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Checkbox Uncheck action.