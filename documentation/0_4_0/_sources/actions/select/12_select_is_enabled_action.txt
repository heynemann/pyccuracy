==============================
I see "some" select is enabled
==============================

Syntax
------
::

	I see "<select name>" select is enabled

where:
	``<select name>`` - name or id for the desired select
	
Description
-----------
Asserts that the specified select is enabled.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the select is disabled (contains attribute "disabled").
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "selSomething" select is enabled
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.2
   Select Is Enabled action.
