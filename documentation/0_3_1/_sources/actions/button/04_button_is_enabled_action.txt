==============================
I see "some" button is enabled
==============================

Syntax
------
::

	I see "<button name>" button is enabled

where:
	``<button name>`` - name or id for the desired input type="button" or input type="submit" or button
	
Description
-----------
Asserts that the specified button is enabled.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the button is disabled.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "btnDoSomething" button is enabled
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.2
   Button Is Enabled action.