=========================
I see "some" radio button
=========================

Syntax
------
::

	I see "<button name>" radio button

where:
	``<button name>`` - name or id for the desired input type="radio"
	
Description
-----------
Asserts that the specified radio button exists **AND** is visible.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.
   
.. warning::

    If a name is specified and more than one radio button is returned the test will fail. If you have more than one radio with the same name, either specify an Id or use 'I see "some" radio button with value of "something"'.

Raises
------
Raises ActionFailedError if the radio button does not exist or is not visible.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "rdbSomething" radio button
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.5
   Radio Button Is Visible action.
