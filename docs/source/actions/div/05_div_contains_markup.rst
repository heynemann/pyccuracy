=======================================
I see "some" div contains "some" markup
=======================================

Syntax
------
::

	I see "<div name>" div contains "<expected markup>"

where:
	``<div name>`` - name or id for the desired div element
	
	``<expected markup>`` - markup that this action needs to assert on
	
Description
-----------
Asserts that the specified div's current markup (HTML Contents) contains the expected markup.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. note::

   This is not an exact match comparison. This means that if the expected markup is a sub-set of the current markup, this action will succeed (if the current markup is "<p>some</p> markup" and the expected text is "<p>some</p>" the action succeeds).


Raises
------
Raises ActionFailedError if the div's markup does not contain the expected markup.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "divSomething" div contains "<p>some</p>" markup
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4
   Div Contains Markup action.
