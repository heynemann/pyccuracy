==================================================
I see "some" image does not have src of "some.gif"
==================================================

Syntax
------
::

	I see "<image name>" image does not have src of "<src>"

where:
	``<image name>`` - name or id for the desired image 
	
	``<src>`` - expected value of src attribute
	
Description
-----------
Asserts that the specified image does not have the expected src (current src is anything other than the specified one).

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. note::

   The src comparison is **Case-Insensitive**.
   
Raises
------
Raises ActionFailedError if the image's src is exactly the specified.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "imgSomething" image does not have src of "check.gif"
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.5
   Image Does Not Have Src Action.
