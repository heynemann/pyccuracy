===================
I see "some" button
===================

Syntax
------
::

	I see "<button name>" button

where:
	``<button name>`` - name or id for the desired input type="button" or input type="submit" or button
	
Description
-----------
Asserts that the specified button exists **AND** is visible.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the button does not exist or is not visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "btnDoSomething" button
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Button Is Visible action.