=================
I see "some" link
=================

Syntax
------
::

	I see "<link name>" link

where:
	<link name> - name for the desired link (anchor)
	
Description
-----------
Asserts that the specified link(anchor) exists **AND** is visible.

Raises
------
Raises ActionFailedError if the link does not exist or is not visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Example
-------
::

	...
	Then
		I see "lnkSomething" link
	
*Rest of the test ommitted for clarity*

.. versionadded:: 0.1
   Link Is Visible action.