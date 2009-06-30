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

import time

from pyccuracy.page import PageRegistry, Page
from pyccuracy.actions import ActionBase
from pyccuracy.languages import LanguageItem

class PageGoToAction(ActionBase):
    '''Navigates to a page or url.'''
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
    '''Changes the current page without actually navigating to it.'''
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
    '''Verifies that the current page's title matches the specified one. Raises otherwise.'''
    regex = LanguageItem('page_see_title_regex')

    def execute(self, context, title):
        expected_title = context.browser_driver.get_title()
        if (title != expected_title):
            raise self.failed(context.language.format("page_see_title_failure", title, expected_title))

class PageCheckContainsMarkupAction(ActionBase):
    regex = LanguageItem("page_check_contains_markup_regex")

    def execute(self, context, expected_markup):
        html = context.browser_driver.get_html_source()

        if expected_markup not in html:
            msg = context.language.format("page_check_contains_markup_failure", expected_markup)
            raise self.failed(msg)

class PageCheckDoesNotContainMarkupAction(ActionBase):
    regex = LanguageItem("page_check_does_not_contain_markup_regex")

    def execute(self, context, expected_markup):
        html = context.browser_driver.get_html_source()

        if expected_markup in html:
            msg = context.language.format("page_check_does_not_contain_markup_failure", expected_markup)
            raise self.failed(msg)

class PageSeeTitleAction(ActionBase):
    regex = LanguageItem("page_see_title_regex")

    def execute(self, context, title):
        actual_title = context.browser_driver.get_title()
        if (actual_title != title):
            msg = context.language.format("page_see_title_failure", actual_title, title)
            raise self.failed(msg)

class PageWaitForPageToLoadAction(ActionBase):
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
    regex = LanguageItem("page_wait_for_seconds_regex")

    def execute(self, context, timeout):
        try:
            timeout = float(timeout)
        except ValueError:
            raise self.failed("The specified time cannot be parsed into a float number: %s" % timeout)

        time.sleep(timeout)

