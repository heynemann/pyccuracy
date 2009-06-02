========
Customizing Pyccuracy
========

Introduction
------------

This page will guide you to Pyccuracy internals, teaching,
step-by-step, how to write custom:

 * Actions, making your tests even more readable and automated.
 * Pages, the Pyccuracy way to register custom elements for a specific url. Once again, aimed on readability.
 * Browser drivers, if you decide to implement your own browser driver, make pyccuracy work with other acceptance testing tools than Selenium. (I.e: Webdriver, HTMLUnit, and so on...)

Custom Actions
--------------

Since version 0.6 Pyccuracy adopted a new declarative approach for creating Actions.::

 >>> from pyccuracy import ActionBase
 >>> class TitleIsFromBrandAction(ActionBase):
 ...     regex = r'^(And )?I see that the title contains (?P<name>Google|Twitter|Pyccuracy) brand$'
 ...     def execute(self, context, name, *args):
 ...         if name not in context.browser_driver.get_title():
 ...             self.fail('The current page does not contains the brand %s' % brand)
 ...


That's all!
You just need to use this action in your tests!
