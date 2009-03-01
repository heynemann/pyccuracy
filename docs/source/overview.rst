========
Overview
========

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

Even with good unit test coveragee, you still need acceptance tests.

The reason behind this is that they aim at different targets. While unit tests aim at proving that your code does
what it should do, acceptance tests prove that your application does what the client expects.

Aside from that, unit tests are mocked tests, meaning that they can't depend on any external resources, while acceptance
tests are *wired* tests, meaning they use your application in the same way the client is going to use it.

So, saying you don't need acceptance tests because you got good unit test coverage is nonsense.

Behavior-Driven Testing
-----------------------

Advantages
==========

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

Plans for the Future
--------------------

Conclusion
----------

