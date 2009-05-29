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

from pyccuracy.page import Page
from pyccuracy.actions import ActionBase
from pyccuracy.languages import LanguageItem

class PageSeeTitle(ActionBase):
    regex = LanguageItem('page_see_title_regex')

    def execute(self, context, title, *args):
        expected_title = context.browser_driver.get_title()
        if (title != expected_title):
            raise PageSeeTitle.Failed(context.language.format("page_see_title_failure", title, expected_title))

class PageGoToAction(ActionBase):
    regex = LanguageItem('page_go_to_regex')

    def execute(self, context, url, *args):
        base_url = context.base_url

#        if url.replace(" ", "") in context.all_pages:
#            context.current_page = context.all_pages[url.replace(" ", "")]
#            url = context.current_page.url
# 
#        if base_url:
#            url = basejoin(base_url + "/", url)
# 
#        protocol, page_name, file_name, complement, querystring, anchor = urllib2.urlparse.urlparse(url)
 
#        if not protocol:
#            if not base_url and os.path.exists(abspath(join(context.tests_dir, url))):
#                url = "file://" + abspath(join(context.tests_dir, url))
#            elif os.path.exists(url):
#                url = "file://" + abspath(url)
#            else:
#                checker = URLChecker()
#                checker.set_url(url)
#                if not checker.is_valid():
#                    raise ActionFailedError(self.language['page_go_to_failure'] % url)

        context.browser_driver.page_open(url)
        context.browser_driver.wait_for_page()


