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

from pyccuracy.result import Result
from pyccuracy.common import Context

class StoryRunner(object):
    def run_stories(self, settings, fixture):
        #No tests to run
        if len(fixture.stories) == 0:
            return Result.empty()

        for story in fixture.stories:
            for scenario in fixture.scenarios:
                context = self.create_context_for(settings)
                for action in scenario.givens + scenario.whens + scenario.thens:
                    pass

        return Result(fixture)

    def create_context_for(self, settings):
        return Context(settings)
