========================
I do not see "some" link
========================

Syntax
------
::

	I do not see "<link name>" link

where:
	``<link name>`` - name or id for the desired link (anchor)
	
Description
-----------
Asserts that the specified link(anchor) does not exist **OR** is not visible.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the link exists AND is visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I do not see "lnkSomething" link
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Link Is Not Visible action.