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

import traceback

from pyccuracy.result import Result
from pyccuracy.common import Context
from pyccuracy.errors import ActionFailedError

class StoryRunner(object):
    def run_stories(self, settings, fixture, context=None):
        for story in fixture.stories:
            for scenario in story.scenarios:
                if not context:
                    context = self.create_context_for(settings)
                for action in scenario.givens + scenario.whens + scenario.thens:
                    result = self.execute_action(context, action)
                    if not result:
                        break

        return Result(fixture=fixture)

    def execute_action(self, context, action):
        try:
            action.execute_function(context, *action.args, **action.kwargs)
        except ActionFailedError, err:
            action.mark_as_failed(err)
            return False
        except Exception, err:
            raise ValueError("Error executing action %s - %s" % (action.execute_function, traceback.format_exc(err)))
        action.mark_as_successful()
        return True

    def create_context_for(self, settings):
        return Context(settings)
