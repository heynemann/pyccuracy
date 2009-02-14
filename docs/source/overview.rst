========
Overview
========

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