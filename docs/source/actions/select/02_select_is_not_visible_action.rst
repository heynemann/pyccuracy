==========================
I do not see "some" select
==========================

Syntax
------
::

	I do not see "<select name>" select

where:
	``<select name>`` - name or id for the desired select element
	
Description
-----------
Asserts that the specified select does not exist **OR** is not visible.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.


Raises
------
Raises ActionFailedError if the select exists AND is visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I do not see "selSomething" select
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Select Is Not Visible action.