=====================
I click "some" button
=====================

Syntax
------
::

	I click "<button name>" button

where:
	``<button name>`` - name for the desired input type="button" or input type="submit" or button
	
Description
-----------
Clicks the specified button.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. warning::

   If the specified element is not found this action will fail.
	
Examples
--------
::

	...
	When
		I click "btnDoSomething" button
	...
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Button Click action.