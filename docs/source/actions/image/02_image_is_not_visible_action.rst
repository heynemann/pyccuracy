=========================
I do not see "some" image
=========================

Syntax
------
::

    I do not see "<image name>" image

where:
    ``<image name>`` - name or id for the desired image

Description
-----------
Asserts that the specified image does not exist **OR** is not visible.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the image exists or is visible.
This Exception is captured by Pyccuracy to assert that the test failed.

Examples
--------
::

    ...
    Then
        I do not see "imgSomething" image

*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4
   Image Is Not Visible Action.
