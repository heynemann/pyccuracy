# -*- coding: utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

