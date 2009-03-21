======================
I wait for 0.5 seconds
======================

Syntax
------
::

	I wait for <number_of_seconds> seconds

where:
	``<number_of_seconds>`` - Number of seconds to keep waiting.
	
Description
-----------
Sleeps for the amount of seconds specified in the number_of_seconds argument. If number_of_seconds is a fraction, waits for that fraction of seconds.
		
Examples
--------

::

	...
	When
		I click "some" image
		And I wait for 0.5 seconds
	Then
		...
		
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4
   Wait For Seconds action.
