===============================
I see "some" button is disabled
===============================

Syntax
------
::

	I see "<button name>" button is disabled

where:
	``<button name>`` - name or id for the desired input type="button" or input type="submit" or button
	
Description
-----------
Asserts that the specified button is disabled.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the button is enabled.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "btnDoSomething" button is disabled
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.2
   Button Is Disabled action.