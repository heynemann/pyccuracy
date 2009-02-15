====================
I click "some" image
====================

Syntax
------
::

	I click "<image name>" image

where:
	``<image name>`` - name or id for the desired image
	
Description
-----------
Clicks the specified image.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. warning::

   If the specified element is not found this action will fail.
   
.. warning::

   This action **DOES NOT** wait for the page to load afterwards. If your image posts or redirects the page somewhere use the Wait For Page To Load Action.
	
Examples
--------
::

	...
	When
		I click "imgDoSomething" image
	...
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Image Click action.