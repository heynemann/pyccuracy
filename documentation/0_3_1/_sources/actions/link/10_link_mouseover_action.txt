=======================
I mouseover "some" link
=======================

Syntax
------
::

	I mouseover "<link name>" link

where:
	``<link name>`` - name or id for the desired link (anchor)
	
Description
-----------
Fires the mouseover event for the specified link.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
      	
Examples
--------
::

	...
	When
		I mouseover "lnkSomething" link
	...
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.3
   Link Mouseover Action.
