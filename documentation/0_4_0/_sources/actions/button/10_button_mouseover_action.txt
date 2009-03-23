=========================
I mouseover "some" button
=========================

Syntax
------
::

	I mouseover "<button name>" button

where:
	``<button name>`` - name or id for the desired input type="button" or input type="submit" or button
	
Description
-----------
Fires the mouseover event for the specified button.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
	
Examples
--------
::

	...
	When
		I mouseover "btnDoSomething" button
	...
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.3
   Button Mouseover action.
