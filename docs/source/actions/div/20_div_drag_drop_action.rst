========================================
I drag the "some" div to the "other" div
========================================

Syntax
------
::

    I drag the "<from div name>" div to the "<to div name>" div

where:
    ``<from div name>`` - name or id for the div to drag
    
    ``<to div name>`` - name or id for the div to drop the <from div name> into

Description
-----------
Drags a div to some other div.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Examples
--------
::

    ...
    When
        I drag the "divNews" div to the "divArea" div
    ...
    
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.4.2
   Drag element added.
