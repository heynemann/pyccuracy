from os.path import join
from os.path import split
from os.path import exists
from os import remove
from os import curdir
from datetime import datetime
import time
from StringIO import StringIO

from lxml import etree
from lxml.etree import Element
from lxml.builder import E
from lxml import etree as ET

VERSION = "0.3.3"

def generate_report(file_path, test_result, language):
    xslt = open(join(split(__file__)[0], "xslt/AccuracyReport.xslt"))
    xslt_doc = etree.parse(xslt)
    transform = etree.XSLT(xslt_doc)
    doc = generate_xml(test_result, language)
    result_tree = transform(doc)

    if exists(file_path):
        remove(file_path)
    
    html = open(file_path, "w")
    html.write(str(result_tree))
    html.close()
    
def generate_xml(test_result, language):
    total_stories = float(test_result.successful_stories + test_result.failed_stories)
    total_scenarios = float(test_result.successful_scenarios + test_result.failed_scenarios)
    percentage_successful_stories = (test_result.successful_stories / (total_stories or 1)) * 100
    percentage_failed_stories = (test_result.failed_stories / (total_stories or 1)) * 100
    percentage_successful_scenarios = (test_result.successful_scenarios / (total_scenarios or 1)) * 100
    percentage_failed_scenarios = (test_result.failed_scenarios / (total_scenarios or 1)) * 100
    
    index = 0
    stories = []
    for story in test_result.stories:
        index += 1
        stories.append(__generate_story(story, index, language))
        
    doc = E.report(
        E.header(
            {
                "date":datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
        ),
        E.footer(
            {
                "version":VERSION
            }
        ),
        E.summary(
            {
                "totalStories":"%.0f" % total_stories,
                "totalScenarios":"%.0f" % total_scenarios,
                "successfulScenarios":str(test_result.successful_scenarios),
                "failedScenarios":str(test_result.failed_scenarios),
                "percentageSuccessful": "%.2f" % percentage_successful_scenarios,
                "percentageFailed": "%.2f" % percentage_failed_scenarios
            }
        )
    )
    
    stories_doc = Element("stories")
    
    for story in stories:
        stories_doc.append(story)
    
    doc.append(stories_doc)
    
    #print etree.tostring(doc, pretty_print=True)
    return doc

def __generate_story(story, story_index, language):
    scenarios = []
    for scenario in story.scenarios:
        scenarios.append(__generate_scenario(scenario, language))
        
    story_doc = E.story(
                    {
                        "index":str(story_index),
                        "asA": "%s %s" % (language["as_a"], story.as_a),
                        "iWant": "%s %s" % (language["i_want_to"], story.i_want_to),
                        "soThat": "%s %s" % (language["so_that"], story.so_that),
                        "isSuccessful": (story.status == "SUCCESSFUL" and "true" or "false")
                    }
                )
                
    for scenario in scenarios:
        story_doc.append(scenario)
        
    return story_doc

def __generate_scenario(scenario, language):
    if scenario.status == "SUCCESSFUL":
        scenario_total_time = (scenario.end_time - scenario.start_time)
        scenario_finish_time = time.asctime(time.localtime(scenario.end_time))
    else:
        scenario_total_time = 0.0
        scenario_finish_time = "FAILED"
    
    actions = []
    odd = True
    actions.append(__generate_given(language, odd))
    odd = not odd
    for action in scenario.givens:
        actions.append(__generate_action(action, language, odd))
        odd = not odd
        
    actions.append(__generate_when(language, odd))
    odd = not odd
    for action in scenario.whens:
        actions.append(__generate_action(action, language, odd))
        odd = not odd
    
    actions.append(__generate_then(language, odd))
    odd = not odd
    for action in scenario.thens:
        actions.append(__generate_action(action, language, odd))
        odd = not odd
        
    #action_text = "".join([etree.tostring(action, pretty_print=False) for action in actions]).replace('"', '&quot;')
        
    scenario_status = scenario.status == "SUCCESSFUL" and "true" or "false"
    
    scenario_doc = E.scenario(
                                {
                                    "index":str(scenario.index),
                                    "description":scenario.title,
                                    "totalTime": "%.2f" % (scenario_total_time),
                                    "finishTime":scenario_finish_time,
                                    "isSuccessful":scenario_status
                                }
                           )
                           
    for action in actions:
        scenario_doc.append(action)
        
    return scenario_doc

def __generate_given(language, odd):
    return __generate_condition(language["given"], odd)

def __generate_when(language, odd):
    return __generate_condition(language["when"], odd)

def __generate_then(language, odd):
    return __generate_condition(language["then"], odd)
    
def __generate_condition(condition_name, odd):
    condition_doc = E.action(
                            {
                                "type":"condition",
                                "description":condition_name,
                                "actionTime":"",
                                "oddOrEven":(odd and "odd" or "even")
                            }
                          )
                          
    return condition_doc
    
def __generate_action(action, language, odd):
    description = action.description
    if action.status == "FAILED":
        description += " - %s" % unicode(action.error)
        
    actionTime = "Unknown"
    if action.status == "SUCCESSFUL" or action.status == "FAILED":
        actionTime = time.asctime(time.localtime(action.start_time))
        
    action_doc = E.action(
                        {
                            "type":"action",
                            "status":action.status,
                            "description": description,
                            "actionTime":actionTime,
                            "oddOrEven":(odd and "odd" or "even")
                        }
                 )
    return action_doc
    
