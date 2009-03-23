======================================
I fill "some" textbox with "some text"
======================================

Syntax
------
::

	I fill "<textbox name>" textbox with "<text>"

where:
	``<textbox name>`` - name or id for the desired input type="text" or textarea.
	
	``<text>`` - text to fill the textbox with. 
	
Description
-----------
Fills the specified textbox or textarea with the given text.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. warning::

   If the specified element is not found this action will fail.
   
.. warning::

	The text currently in the textbox or textarea is replaced by the new text.
	
Examples
--------
::

	...
	When
		I fill "txtQuery" textbox with "some new text"
	...
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Textbox Type action.