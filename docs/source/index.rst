=========================
Welcome to Pyccuracy Docs
=========================

Documentation Contents
----------------------

.. toctree::
   :maxdepth: 1

   overview
   tutorial
   
.. toctree::
   :maxdepth: 3
   
   actions
   
Introduction
------------

Pyccuracy is a Behavior-Driven Design Acceptance Testing framework. 

Pyccuracy uses an external DSL to express tests. This has the advantage of creating clean, readable tests.

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

There are some advantages of using an external DSL as well as disadvantages (isn't life fun?).

The major advantage is how clear you can read this. The readability is a major concern for Pyccuracy tests. 
Another advantage is that since we're defining the language ourselves we're not constrained to the programming language idiosyncracies.

One disadvantage of the external DSL is tool support. As of now you have to know the available constructs and use them properly. 
In future versions we'll work on validators and coloring/completion for main tools (no promises, ok?). 
The best way to get the tool you use to support Pyccuracy is implement the support and contribute to the project. 
The second best way is to create a ticket for it and vote for it.