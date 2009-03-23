================================
I see "some" textbox is disabled
================================

Syntax
------
::

	I see "<textbox name>" textbox is disabled

where:
	``<textbox name>`` - name or id for the desired textbox element
	
Description
-----------
Asserts that the specified textbox is disabled.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the textbox is enabled.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "txtSomething" textbox is disabled
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4
   Textbox Is Disabled action.
