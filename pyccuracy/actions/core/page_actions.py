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

'''Page actions are actions that have a specific impact in the browser, like navigating to a different page.

This is a *very important* category of actions, since almost any single test relies on navigating to a given page.'''

import time

from pyccuracy.page import PageRegistry, Page
from pyccuracy.actions import ActionBase
from pyccuracy.languages import LanguageItem

class PageGoToAction(ActionBase):
    '''h3. Examples

  * And I go to My Custom Page
  * And I go to "http://www.google.com"

h3. Description

This action tells Pyccuracy that the current browser driver ([[Creating a custom Browser Driver]]) should navigate to the URL that's registered in the specified page. Other than that, it also changes that current page in Pyccuracy's context to the specified one. This means that Pyccuracy will start using the registered elements and url in the specified page. 

For more information on creating custom pages check the [[Creating custom Pages]] page.

If you specify an url directly, Pyccuracy sets the current page to None and you can't use registered elements. That might make sense for some scenarios, but is the least preferred way of using this action.

This action also issues automatically a wait for page to load action after navigating. This is important to make sure that the following actions work with a properly loaded page.'''
    __builtin__ = True
    regex = LanguageItem('page_go_to_regex')

    def execute(self, context, url):
        page, resolved_url = PageRegistry.resolve(context.settings, url.replace('"', ''), must_raise=False)

        if not resolved_url or (not url.startswith('"') and not page):
            raise self.failed(context.language.format("page_go_to_failure", url))

        context.browser_driver.page_open(resolved_url)
        context.browser_driver.wait_for_page()
        context.url = resolved_url
        if page:
            # If the resolved page is the same as the current one, 
            # there's not need to override the context page, risking
            # losing all the re-registered elements of the users.
            if not isinstance(context.current_page, page):
                context.current_page = page()
                if hasattr(context.current_page, "register"):
                    context.current_page.register()

class PageAmInAction(ActionBase):
    '''h3. Example

  * And I am in My Custom Page

h3. Description

This action tells Pyccuracy that it should change the current page (as far as registered elements and url go) to a given page.

The same rule for direct urls of Go to Page applies to this action.

Other than that, this action does not do anything. The main purpose of this action is responding to some client event or redirect that might have changed the current page without our direct action (like submitting a form that redirects us to a different page).'''
    __builtin__ = True
    regex = LanguageItem("page_am_in_regex")

    def execute(self, context, url):
        page, resolved_url = PageRegistry.resolve(context.settings, url, must_raise=False)

        if page:
            # If the resolved page is the same as the current one, 
            # there's not need to override the context page, risking
            # losing all the re-registered elements of the users.
            if not isinstance(context.current_page, page):
                context.current_page = page()
                if hasattr(context.current_page, "register"):
                    context.current_page.register()
            context.url = resolved_url
        else:
            raise self.failed(context.language.format("page_am_in_failure", url))

class PageSeeTitleAction(ActionBase):
    '''h3. Example

  * And I see "whatever" title

h3. Description

This action asserts that the currently loaded page's title (Browser title) is the specified one. '''
    __builtin__ = True
    regex = LanguageItem("page_see_title_regex")

    def execute(self, context, title):
        actual_title = context.browser_driver.get_title()
        if (actual_title != title):
            msg = context.language.format("page_see_title_failure", actual_title, title)
            raise self.failed(msg)

class PageCheckContainsMarkupAction(ActionBase):
    '''h3. Example

  * And I see that current page contains "&lt;p&gt;expected markup&lt;/p&gt;"

h3. Description

This action asserts that the currently loaded page's mark-up contains the given mark-up.'''
    __builtin__ = True
    regex = LanguageItem("page_check_contains_markup_regex")

    def execute(self, context, expected_markup):
        html = context.browser_driver.get_html_source()

        if expected_markup not in html:
            msg = context.language.format("page_check_contains_markup_failure", expected_markup)
            raise self.failed(msg)

class PageCheckDoesNotContainMarkupAction(ActionBase):
    '''h3. Example

  * And I see that current page does not contain "&lt;p&gt;expected markup&lt;/p&gt;"

h3. Description

This action asserts that the currently loaded page's mark-up *does not* contain the given mark-up.'''
    __builtin__ = True
    regex = LanguageItem("page_check_does_not_contain_markup_regex")

    def execute(self, context, expected_markup):
        html = context.browser_driver.get_html_source()

        if expected_markup in html:
            msg = context.language.format("page_check_does_not_contain_markup_failure", expected_markup)
            raise self.failed(msg)

class PageWaitForPageToLoadAction(ActionBase):
    '''h3. Examples

  * And I wait for the page to load
  * And I wait for the page to load for 5 seconds

h3. Description

This action instructs the browser driver to wait for a given number of seconds for the page to load. If it times out, the test fails.'''
    __builtin__ = True
    regex = LanguageItem("page_wait_for_page_to_load_regex")

    def execute(self, context, timeout):
        try:
            timeout = float(timeout)
        except Exception:
            timeout = None

        if timeout:
            context.browser_driver.wait_for_page(timeout * 1000)
        else:
            context.browser_driver.wait_for_page()

class PageWaitForSecondsAction(ActionBase):
    '''h3. Examples

  * And I wait for 5 seconds
  * And I wait for 1 second
  * And I wait for 3.5 seconds

h3. Description

This action is just a proxy to Python's time.sleep function. It just hangs for a given number of seconds.'''
    __builtin__ = True
    regex = LanguageItem("page_wait_for_seconds_regex")

    def execute(self, context, timeout):
        try:
            timeout = float(timeout)
        except ValueError:
            raise self.failed("The specified time cannot be parsed into a float number: %s" % timeout)

        time.sleep(timeout)

