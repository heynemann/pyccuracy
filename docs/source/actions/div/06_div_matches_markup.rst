======================================
I see "some" div matches "some" markup
======================================

Syntax
------
::

	I see "<div name>" div matches "<expected markup>"

where:
	``<div name>`` - name or id for the desired div element
	
	``<expected markup>`` - markup that this action needs to assert on
	
Description
-----------
Asserts that the specified div's current markup (HTML Contents) contains exactly the expected markup.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. note::

   This is an exact match comparison. This means that if the current markup is anything other than exactly the expected markup, this action will fail (if the current markup is "<p>some</p> markup" and the expected markup is "<p>some</p> markup" the action succeeds).


Raises
------
Raises ActionFailedError if the div's markup does not match exactly the expected markup.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "divSomething" div matches "<p>some</p> markup" markup
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.5
   Div Matches Markup action.
