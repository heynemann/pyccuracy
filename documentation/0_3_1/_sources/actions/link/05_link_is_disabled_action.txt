=============================
I see "some" link is disabled
=============================

Syntax
------
::

	I see "<link name>" link is disabled

where:
	``<link name>`` - name or id for the desired link (anchor)
	
Description
-----------
Asserts that the specified link(anchor) is disabled.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the link is enabled (does not contain attribute "disabled").
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "lnkSomething" link is disabled
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.2
   Link Is Disabled action.