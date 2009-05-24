================================================
I wait for "some" div to disappear for 5 seconds
================================================

Syntax
------
::

    I wait for "<div name>" div to disappear
    I wait for "<div name>" div to disappear for <float number of seconds> seconds

where:
    ``<div name>`` - name or id for the desired div

    ``<float number of seconds>`` - number of seconds to wait for the element to disappear. This portion is optional.

Description
-----------
Waits for the element to disappear for a given number of seconds. After this timeout the action fails. The default timeout is 5 seconds.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Examples
--------
::

    ...
    When
        I wait for "divWaitForVisible" div to disappear for 10 seconds
    ...
    
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4.2
   Wait for div to disappear.
