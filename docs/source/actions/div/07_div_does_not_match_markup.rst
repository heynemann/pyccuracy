=============================================
I see "some" div does not match "some" markup
=============================================

Syntax
------
::

	I see "<div name>" div does not match "<expected markup>" markup

where:
	``<div name>`` - name or id for the desired div element
	
	``<expected markup>`` - markup that this action needs to assert on
	
Description
-----------
Asserts that the specified div's current markup (HTML Contents) contains anything other than the expected markup.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. note::

   This is an exact match comparison. This means that if the current markup is anything other than exactly the expected markup, this action will succeed (if the current markup is "<p>some</p> markup" and the expected markup is "<p>some</p> markup" the action fails).


Raises
------
Raises ActionFailedError if the div's markup matches exactly the expected markup.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "divSomething" div does not match "<p>some</p> markup" markup
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.5
   Div Does Not Match Markup action.
