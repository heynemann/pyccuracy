=================
I see "some" link
=================

Syntax
------
::

	I see "<link name>" link

where:
	``<link name>`` - name or id for the desired link (anchor)
	
Description
-----------
Asserts that the specified link(anchor) exists **AND** is visible.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the link does not exist or is not visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "lnkSomething" link
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Link Is Visible action.