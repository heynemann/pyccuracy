=================================
I see "some" link has "some" href
=================================

Syntax
------
::

	I see "<link name>" link has "<href>" href 

where:
	``<link name>`` - name or id for the desired link (anchor)
	
	``<href>`` - expected value of href attribute
	
Description
-----------
Asserts that the specified link(anchor) has the expected href.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. note::

   The href comparison is **Case-Insensitive**.
   
Raises
------
Raises ActionFailedError if the link's href is different than the expected.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "lnkSomething" link has "http://www.google.com" href
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.3
   Link Has Href Action.
