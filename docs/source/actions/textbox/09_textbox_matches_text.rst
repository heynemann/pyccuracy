========================================
I see "some" textbox matches "some text"
========================================

Syntax
------
::

	I see "<textbox name>" textbox matches "<expected text>"

where:
	``<textbox name>`` - name or id for the desired textbox element
	
	``<expected text>`` - text that this action needs to assert on
	
Description
-----------
Asserts that the specified textbox current text matches exactly the expected text.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match,
   the element is deemed not available.
   
.. note::

   This is an exact match comparison.
   This means that if the expected text is not exactly the same as the current text (case-insensitive comparison),
   this action will fail (if the current text is "some large text" and the expected text is anything other than that,
   the action fails).


Raises
------
Raises ActionFailedError if the textbox's text does not match exactly the expected text.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "txtSomething" textbox matches "some text"
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.2
   Textbox Matches Text action.
