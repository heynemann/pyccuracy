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

from pyccuracy.result import Result
from pyccuracy.common import Context
from pyccuracy.errors import ActionFailedError

class StoryRunner(object):
    def run_stories(self, settings, fixture):
        #No tests to run
        if len(fixture.stories) == 0:
            return Result.empty()

        for story in fixture.stories:
            for scenario in story.scenarios:
                context = self.create_context_for(settings)
                for action in scenario.givens + scenario.whens + scenario.thens:
                    try:
                        action.execute_function(context, *action.args, **action.kwargs)
                    except ActionFailedError, err:
                        action.mark_as_failed(err)
                    action.mark_as_successful()

        return Result(fixture)

    def create_context_for(self, settings):
        return Context(settings)
