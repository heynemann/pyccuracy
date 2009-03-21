=======================
I do not see "some" div
=======================

Syntax
------
::

	I do not see "<div name>" div

where:
	``<div name>`` - name or id for the desired div
	
Description
-----------
Asserts that the specified div does not exist or is invisible.

.. note::

   The specified name will be checked against both "name" and "id" values.
   Only if neither of those match, the element is deemed not available.

.. note::

   Invisible here means style="display:none" or style="visibility:hidden".

Raises
------
Raises ActionFailedError if the div exists **AND** is visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I do not see "divSomething" div
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.2
   Div Is Not Visible action.