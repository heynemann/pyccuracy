def pre_story(context, story): 
    fileHandle = open ('pre_post_scripts_test.txt', 'a') 
    fileHandle.write("%s - As a %s I want to %s So that %s\n" % ("Pre Story", story.as_a, story.i_want_to, story.so_that))
    fileHandle.close()

def pre_scenario(context, story, scenario): 
    fileHandle = open ('pre_post_scripts_test.txt', 'a') 
    fileHandle.write("%s - Scenario %s - %s\n" % ("Pre Scenario", scenario.index, scenario.title))
    fileHandle.close()

def post_scenario(context, story, scenario, result): 
    fileHandle = open ('pre_post_scripts_test.txt', 'a') 
    fileHandle.write("%s - Scenario %s - %s\n" % ("Post Scenario", scenario.index, scenario.title))
    fileHandle.close()

def post_story(context, story, result): 
    fileHandle = open ('pre_post_scripts_test.txt', 'a') 
    fileHandle.write("%s - As a %s I want to %s So that %s\n" % ("Post Story", story.as_a, story.i_want_to, story.so_that))
    fileHandle.close()

