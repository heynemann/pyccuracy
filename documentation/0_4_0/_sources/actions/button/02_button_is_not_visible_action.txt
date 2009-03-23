==========================
I do not see "some" button
==========================

Syntax
------
::

	I do not see "<button name>" button

where:
	``<button name>`` - name or id for the desired input type="button" or input type="submit" or button
	
Description
-----------
Asserts that the specified button does not exist or is invisible.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

.. note::

   Invisible here means style="display:none" or style="visibility:hidden".

Raises
------
Raises ActionFailedError if the button exists **AND** is visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I do not see "btnDoSomething" button
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.2
   Button Is Not Visible action.