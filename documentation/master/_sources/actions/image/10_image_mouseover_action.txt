======================
I mouseover "some" image
======================

Syntax
------
::

	I mouseover "<image name>" image

where:
	``<image name>`` - name or id for the desired image
	
Description
-----------
Fires the mouseover event for the specified image.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
	
Examples
--------
::

	...
	When
		I mouseover "imgDoSomething" image
	...
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.3
   Image Mouseover action.
