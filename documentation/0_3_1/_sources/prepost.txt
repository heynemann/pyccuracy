=================================
Test/Scenario Pre/Post Conditions
=================================

Introduction
------------

Pyccuracy supports writing pre and post events code in python.

The intention behind this is that you can create data or anything else that allows you to put the system in a known state for a given story or scenario.

It's extremely easy to write pre and post event hooks for a given test (*.acc) file. Just create a file with the exact same file name, but with a .py extension.

File Format
-----------

The format for the events file should be::
    
    def pre_story(context, story): 
        pass

    def pre_scenario(context, story, scenario): 
        '''This gets executed before each scenario'''
        pass

    def post_scenario(context, story, scenario, result): 
        '''This gets executed after each scenario'''
        pass
        
    def post_story(context, story, result): 
        pass

None of the methods above is required. You can specify only the ones that actually matter for you.

Compiled Files
--------------

Pyccuracy will first look for a .pyc file, then for a .py file. 

The reasoning behind this is that there's a chance that you'll only have the compiled one.

Conclusion
----------

Writing pre and post event hooks allow you to fine-tune execution of each test.

Changelog
---------
.. versionadded:: 0.3
   Pre and Post event hooks.
