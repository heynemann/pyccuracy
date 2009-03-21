=================================
I see "some" link has "some" text
=================================

Syntax
------
::

	I see "<link name>" link has "<text>" text 

where:
	``<link name>`` - name or id for the desired link (anchor)
	
	``<text>`` - expected text
	
Description
-----------
Asserts that the specified link(anchor) has the expected text.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. note::

   The text comparison is **Case-Insensitive**.
   
Raises
------
Raises ActionFailedError if the link's text is different than the expected.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "lnkSomething" link has "Click me" text
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.3
   Link Has Text Action.
