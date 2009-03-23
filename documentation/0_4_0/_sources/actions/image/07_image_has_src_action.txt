========================================
I see "some" image has src of "some.gif"
========================================

Syntax
------
::

	I see "<image name>" image has src of "<src>"

where:
	``<image name>`` - name or id for the desired image 
	
	``<src>`` - expected value of src attribute
	
Description
-----------
Asserts that the specified image has the expected src.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. note::

   The src comparison is **Case-Insensitive**.
   
Raises
------
Raises ActionFailedError if the image's src is different than the expected.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "imgSomething" image has src of "something.gif"
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4
   Image Has Src Action.
