===========================
I wait for the page to load
===========================

Syntax
------
::

	I wait for the page to load[ for <timeout> seconds]

where:
	``<timeout>`` - optional argument that specifies maximum time to wait for page to load. **Defaults to 20 seconds**.
	
Description
-----------
Waits for the page to load after some action, like clicking an image or any other action that changes the current page to another one (redirection or post).
		
Examples
--------

1) Waits for the page to load using default timeout (20 seconds)

::

	...
	When
		I click "some" image
		And I wait for the page to load
	Then
		...
		
2) Waits for the page to load using a specific timeout

::

	...
	When
		I click "some" image
		And I wait for the page to load for 10 seconds
	Then
		...

*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Wait For Page To Load action.