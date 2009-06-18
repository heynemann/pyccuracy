#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Bernardo Heynemann <heynemann@gmail.com>
# Copyright (C) 2009 Gabriel Falcão <gabriel@nacaolivre.org>
#
# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.opensource.org/licenses/osl-3.0.php
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
from os import remove
from os import curdir

from datetime import datetime
from os.path import join, split, exists

from StringIO import StringIO

from lxml import etree
from lxml.etree import Element
from lxml.builder import E
from lxml import etree as ET

from pyccuracy import Version

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
    total_stories = float(test_result.fixture.count_total_stories())
    total_scenarios = float(test_result.fixture.count_total_scenarios())
    successful_stories = test_result.fixture.count_successful_stories()
    successful_scenarios = test_result.fixture.count_successful_scenarios()
    failed_stories = test_result.fixture.count_failed_stories()
    failed_scenarios = test_result.fixture.count_failed_scenarios()
    percentage_successful_stories = (successful_stories / (total_stories or 1)) * 100
    percentage_failed_stories = (failed_stories / (total_stories or 1)) * 100
    percentage_successful_scenarios = (successful_scenarios / (total_scenarios or 1)) * 100
    percentage_failed_scenarios = (failed_scenarios / (total_scenarios or 1)) * 100

    index = 0
    stories = []
    for story in test_result.fixture.stories:
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
                "version":Version
            }
        ),
        E.summary(
            {
                "totalStories":"%.0f" % total_stories,
                "totalScenarios":"%.0f" % total_scenarios,
                "successfulScenarios":str(successful_scenarios),
                "failedScenarios":str(failed_scenarios),
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
                        "identity":story.identity,
                        "asA":"%s %s" % (language.get("as_a"), story.as_a),
                        "iWant":"%s %s" % (language.get("i_want_to"), story.i_want_to),
                        "soThat":"%s %s" % (language.get("so_that"), story.so_that),
                        "isSuccessful":(story.status == "SUCCESSFUL" and "true" or "false")
                    }
                )

    for scenario in scenarios:
        story_doc.append(scenario)

    return story_doc

def __generate_scenario(scenario, language):
    if scenario.status == "SUCCESSFUL":
        scenario_total_time = scenario.ellapsed()
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
                                    "totalTime": "%.2f" % scenario_total_time,
                                    "finishTime":scenario_finish_time,
                                    "isSuccessful":scenario_status
                                }
                           )

    for action in actions:
        scenario_doc.append(action)

    return scenario_doc

def __generate_given(language, odd):
    return __generate_condition(language.get("given"), odd)

def __generate_when(language, odd):
    return __generate_condition(language.get("when"), odd)

def __generate_then(language, odd):
    return __generate_condition(language.get("then"), odd)

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

