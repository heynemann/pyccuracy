======================
I mouseover "some" div
======================

Syntax
------
::

	I mouseover "<div name>" div

where:
	``<div name>`` - name or id for the desired div
	
Description
-----------
Fires the mouseover event for the specified div.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
	
Examples
--------
::

	...
	When
		I mouseover "divDoSomething" div
	...
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.3
   Div Mouseover action.
