===================
I see "some" button
===================

Syntax
------
::

	I see "<button name>" button

where:
	<button name> - name for the desired input type="button" or input type="submit" or button
	
Description
-----------
Asserts that the specified button exists **AND** is visible.

Raises
------
Raises ActionFailedError if the button does not exist or is not visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Example
-------
::

	...
	Then
		I see "btnDoSomething" button
	
*Rest of the test ommitted for clarity*

.. versionadded:: 0.1
   Button Is Visible action.