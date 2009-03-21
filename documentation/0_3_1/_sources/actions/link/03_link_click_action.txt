===================
I click "some" link
===================

Syntax
------
::

	I click "<link name>" link

where:
	``<link name>`` - name or id for the desired link (anchor)
	
Description
-----------
Clicks the specified link.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. warning::

   If the specified element is not found this action will fail.
   
.. warning::

   After executing this action, the browser driver waits for the page to finish loading.
   
   If you have a link that does not redirect the page (AJAX or Javascript), please use the Link Click No Wait action.
	
Examples
--------
::

	...
	When
		I click "lnkSomewhere" link
	...
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Link Click action.