======================================
I fill "some" textbox with "some text"
======================================

Syntax
------
::

	I fill "<textbox name>" textbox with "<text>"

where:
	<textbox name> - name for the desired input type="text" or textarea.
	<text> - text to fill the textbox with. 
	
Description
-----------
Fills the specified textbox or textarea with the given text.

.. warning::

	The text currently in the textbox or textarea is replaced by the new text.
	
Example
-------
::

	...
	When
		I fill "txtQuery" textbox with "some new text"
	...
	
*Rest of the test ommitted for clarity*

.. versionadded:: 0.1
   Textbox Type action.