================
I see "some" div
================

Syntax
------
::

	I see "<div name>" div

where:
	``<div name>`` - name or id for the desired div
	
Description
-----------
Asserts that the specified div exists **AND** is visible.

.. note::

   The specified name will be checked against both "name" and "id" values.
   Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the div does not exist or is not visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "divSomething" div
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.2
   Div Is Visible action.