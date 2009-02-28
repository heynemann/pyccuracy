=========================================
I see "some" textbox contains "some text"
=========================================

Syntax
------
::

	I see "<textbox name>" textbox contains "<expected text>"

where:
	``<textbox name>`` - name or id for the desired textbox element
	
	``<expected text>`` - text that this action needs to assert on
	
Description
-----------
Asserts that the specified textbox current text contains the expected text.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. note::

   This is not an exact match comparison. This means that if the expected text is a sub-set of the current text, this action will succeed (if the current text is "some large text" and the expected text is "large" the action succeeds).


Raises
------
Raises ActionFailedError if the textbox's text does not contain the expected text.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "txtSomething" textbox contains "some text"
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.2
   Textbox Contains Text action.
