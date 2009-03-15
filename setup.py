# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages
import sys, os

version = '0.3'

setup(name='Pyccuracy',
      version=version,
      description="Pyccuracy is a BDD style Acceptance Testing framework",
      long_description="""\
Introduction
------------

Pyccuracy is a Behavior-Driven Acceptance Testing framework (more on that in the next section).

It serves two crystal clear, yet very hard to achieve, purposes:

    1.  **Encouraging Test-Driven Acceptance Testing**

        This means writing acceptance tests prior to the tasks that describe them.
        This way you take Test-Driven-Development one step further and push yourself
        towards the right direction when it comes to the application UI (user interface).

    2.  **Providing an easy and clear language to write tests**

        It's really important to write acceptance tests that prove your app works.
        Most of the time people don't do it using some (or all) of the excuses below:

        a. Acceptance Tests are fragile - People say they don't do them because they break easily.
        b. Acceptance Tests are slow - Running the acceptance tests take more time than we can afford.
        c. Acceptance Tests are hard to write - The xyz acceptance testing framework being used is too hard to write tests on.
        d. Unit Test Coverage is good enough - We have unit test coverage anyway, so why do Acceptance tests anyway?

Well, all of the above are just lame excuses on why not to write Acceptance tests.

In my point of view, if you can't prove that something works as expected, then it doesn't.
Acceptance tests serve one purpose: Demonstrating, beyond shadow of doubt, that your application
works as the customer expects.

They are real concerns, though. Let's tackle each of them individually.

Acceptance Tests Fragility
==========================

First, the fragility issue. To determine if your tests are fragile, you first need to define a proper fragile test.
In my opinion a fragile acceptance test is one that breaks even though you haven't changed the behavior of the UI
the test works on.

Fragility is often a problem with how you are writing your tests, other than the actual tests.
Acceptance tests need to test behavior. It's ok to write acceptance tests that verify that the UI is in accordance to
any number of standards you define (Pyccuracy even supports that concept). Just bare in mind that these tests
are not acceptance tests. They are smoke tests or whatever you want to call them, and they are going to be **VERY** fragile,
because that's their purpose: breaking if the UI changes. So it's best to have as few of those as you possibly can.

Pyccuracy encourages less-fragile tests by having a concise language, yet expressful, for writing your tests.

Acceptance Tests Running Speed
==============================

Running acceptance tests is always going to be slower than unit tests, for the simple fact that they are wired tests
(meaning they connect to real resources, which are always slower than mocks or stubs).

The key thing here is that slower does not need to translate into slow. Even though we rely a lot
on the underlying testing framework (i.e. Selenium), we've optimised Pyccuracy quite a lot in order to have great performance.

We still need *real* project data in order to determine how slow or fast Pyccuracy really is,
since our test scenarios are too simple for that purpose.

Acceptance Testing Language
===========================

With Pyccuracy, the proposition is that general-purpose programming languages
might not be the best language to describe acceptance tests.

Pyccuracy provides a domain-specific language (DSL) for
writing acceptance tests (you can see an example at the *Sample Test* section). The purpose of using a DSL
is to have clear easy-to-write tests.

This enables scenarios such as a wiki that holds all your tests as well-organized pages or using the acceptance tests to
enable better discussion with clients on what a story should cover.

Pyccuracy uses a Regular-Expression driven approach to the DSL, which makes it really easy to improve and refine the language.

Unit Tests Coverage
===================

Even with good unit test coverage, you still need acceptance tests.

The reason behind this is that they aim at different targets. While unit tests aim at proving that your code does
what it should do, acceptance tests prove that your application does what the client expects.

Aside from that, unit tests are mocked tests, meaning that they can't depend on any external resources, while acceptance
tests are *wired* tests, meaning they use your application in the same way the client is going to use it.

So, saying you don't need acceptance tests because you got good unit test coverage is nonsense.

Behavior-Driven Testing
-----------------------

Behavior-Driven Testing (BDT) is a concept derived from Behavior-Driven Development [#bdd]_.
The information in the Behavior-Driven Development website is well worth your time.

Whereas BDD uses a parallel to Test-Driven Development [#tdd]_ to specify unit tests as scenarios,
BDT uses the same ubiquitous language to describe acceptance tests.

Defining the acceptance tests in a language that's common for both developers and clients alike has many benefits:

    1.  It's very easy to define what a story really represents in terms of business value with the client.
    2.  There's no impedance mismatch between what the developers think a story is and what the client expects.
    3.  The stories get auto-documented as to what their behavior is [#allaboutbehavior]_.
        This is really important as to get new members in the team up to speed faster, as well
        as to increase confidence when performing refactoring to the UI.

Language Support
----------------

Pyccuracy also supports multiple languages. This has been a really important goal for Pyccuracy team since release 0.1.

If you want to write clear tests, what clearer language to use than the one you currently speak?

We understand that there are non-english speakers out there doing amazing things, and we want to empower that
(the team behind Pyccuracy 0.1 is composed only of Brazilians - but we encourage anyone anywhere to join).

If your language is not covered in Pyccuracy yet, it's really easy to create a language file.
Shouldn't take more than half an hour. Just contact us using Pyccuracy's e-mail group [#emailgroup]_, and we'll
point you in the right direction.

Currently Supported Languages:

    1.  English
    2.  Português Brasil sem acentos (Portuguese Brazil)

Sample Test
-----------

A typical Pyccuracy test would be something like::

  As a Google User
  I want to search Google
  So that I can test Pyccuracy

  Scenario 1 - Searching for Hello World
  Given
    I go to "http://www.google.com"
  When
    I fill "q" textbox with "Hello World"
    And I click "btnG" button
  Then
    I see "Hello World - Pesquisa Google" title

  Scenario 2 - Searching for Monty Python
  Given
    I go to "http://www.google.com"
  When
    I fill "q" textbox with "Monty Python"
    And I click "btnG" button
  Then
    I see "Monty Python - Pesquisa Google" title

As you can see, that's pretty clear and yet, very intentful.
Without resorting to anything other than the test you could understand what's happening.

Other than that, this test proves an aspect of google (that the specified search text should be in the title).

With a good test suite you can easily cover all business value of your application and use that as prove that your app
does what it should be doing.

Plans for the Future
--------------------

These are some plans that are still under study.

1.  Grid Execution of tests - Since tests are slow(er), we are studying ways of parallelizing their execution,
    thus speeding up the execution of test suites.

2.  Storing tests in a Wiki - Some users requested that tests be stored in medias other than files.
    This presents some issues:
    1.  How to communicate with the wiki - This should probably be easy since there are many wikis out there
        that provide python bindings or service-based operations (or REST).
    2.  How to organize the environments. By organizing we mean how can you provide the developer
        with a way to create the tests locally and then keep migrating them to other wiki instances (Dev, UAT, etc).
        This has to be easy, otherwise this is not a feasible solution.

Conclusion
----------

Pyccuracy should speed up the creation of acceptance tests and improve on the way your dev team communicates with the
client when related to what business value and behavior the stories contain.

Project Cheat Sheet
-------------------

Project Google Groups Page - http://groups.google.com/group/pyccuracy

Project Conventions: http://groups.google.com/group/pyccuracy/web/conventions

Links and Blog Posts: http://groups.google.com/group/pyccuracy/web/Links%20and%20Blog%20Posts

Project JIRA (Issue and Version Management) -
http://jira.stormwindproject.org:8080/browse/PYCCURACY

Project Subversion Server: http://svn.stormwindproject.org/svn/Pyccuracy (``svn
co http://svn.stormwindproject.org/svn/Pyccuracy Pyccuracy``)

**PyPI Page**: http://pypi.python.org/pypi/Pyccuracy/

**Docs for current version**: http://packages.python.org/Pyccuracy/

.. rubric:: Footnotes

.. [#bdd] Behavior-Driven Development - Know more in http://behaviour-driven.org/.
.. [#tdd] Test-Driven Development - Know more in http://en.wikipedia.org/wiki/Test-driven_development.
.. [#allaboutbehavior] It's all about behavior - http://behaviour-driven.org/ItsAllBehaviour
.. [#emailgroup] Google Group for Pyccuracy - http://groups.google.com/group/pyccuracy

=============
Release Notes
=============

Release Notes - Pyccuracy - Version 0.1
---------------------------------------

**Bug**

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-66] - Fix 
running the 
pyccuracy_core on nix machines.

**New Feature**

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-14] - 
Check/Uncheck Checkbox Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-15] - 
Checkbox Is Checked Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-16] - 
Checkbox Is Not Checked Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-17] - 
See Checkbox Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-21] - 
See Button Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-40] - 
See Select Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-41] - 
Do Not See Select Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-42] - 
See Select Has Selected Index of Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-50] - 
Select Option By Index

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-57] - 
Click Image Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-58] - 
See Link Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-63] - 
Do Not See Link Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-64] - 
Click Link Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-80] - 
Render a summary of the run after the run

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-87] - 
Wait for Page To Load Action

**Task**

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-4] - 
Create documentation for current release

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-9] - 
Encapsulate Pyccuracy on a .egg

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-10] - 
Create index page for Pyccuracy.egg distribution

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-84] - 
Add tests for Click Button

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-85] - 
Add tests for Type Text

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-86] - 
Add tests for See Title""",
      classifiers=["Development Status :: 2 - Pre-Alpha",
				   "Intended Audience :: Developers",
				   "License :: OSI Approved",
				   "Natural Language :: English",
				   "Programming Language :: Python :: 2.5",
				   "Topic :: Software Development :: Testing",], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Acceptance Testing Accuracy Behavior Driven Development',
      author='Bernardo Heynemann',
      author_email='heynemann@gmail.com',
      url='http://groups.google.com/group/pyccuracy',
      license='OSI',
      packages=["pyccuracy", "pyccuracy.actions"],
	  package_data = {
        'pyccuracy': ['languages/*.txt', 'lib/*/*.*', 'lib/*/*/*.*', 'lib/*/*/*/*.*'],
	  },
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "selenium>=0.9.2",
          "PyoC>=0.1"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
