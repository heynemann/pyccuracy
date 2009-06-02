===============================
I see "some" select is disabled
===============================

Syntax
------
::

	I see "<select name>" select is disabled

where:
	``<select name>`` - name or id for the desired select
	
Description
-----------
Asserts that the specified select is disabled.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the select is enabled (does not contain attribute "disabled").
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "selSomething" select is disabled
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.2
   Select Is Disabled action.
