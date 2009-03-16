===============================================
I see "some" textbox does not match "some text"
===============================================

Syntax
------
::

	I see "<textbox name>" textbox does not match "<expected text>"

where:
	``<textbox name>`` - name or id for the desired textbox element
	
	``<expected text>`` - text that this action needs to assert on
	
Description
-----------
Asserts that the specified textbox current text does not match the expected text.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match,
   the element is deemed not available.
   
.. note::

   This is an exact match comparison.
   This means that if the expected text is anything other than exactly the same as the current text (case-insensitive comparison),
   this action will fail (if the expected text is "some large text" and the current text is anything other than that,
   the action passes).

Raises
------
Raises ActionFailedError if the textbox's text does not match exactly the expected text.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "txtSomething" textbox does not match "some text"
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.3
   Textbox Does Not Match Text action.
