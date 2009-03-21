==================
I see "some" image
==================

Syntax
------
::

	I see "<image name>" image

where:
	``<image name>`` - name or id for the desired image
	
Description
-----------
Asserts that the specified image exists **AND** is visible.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the image does not exist or is not visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "imgSomething" image
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.3
   Image Is Visible Action.
