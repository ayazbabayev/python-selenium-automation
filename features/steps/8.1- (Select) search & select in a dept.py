from behave import when, then

#   Note:
#   To run select (For selecting books dept in Amazon search:
#   In header.py you import-->     from selenium.webdriver.support.ui import Select
#   Add def into header.py for select menu. select = Select()
#   Find the 'department dropdown box' locator in Amazon: (DEPARTMENT_SELECT)
#   Add locator into header.py under class, use it under def with select shortcut
#   Under select (ex. for books), use select_by_value(...) and paste the VALUE of books in it:
#   value for books: search-alias=stripbooks
#   For verification, we used search_results page.
#   Added NAV_SUBNAV shortcut under class, then used in def. And wrote context code for def below
#   To make the search dynamic, we used {alias} --- like search_word
#   alias name was chosen because all elements in subnav categories start with "search-alias=..."
#   In the end, we turn hardcoded locator for search verification into dynamic locator:
#   #nav-subnav[data-category='books']" <<< here 'books' turns into a dynamic locator: {SUB_STRING}
#   Define the dynamic category, under search_results_page.py

#   def get_subnav_locator(self, category):
#       return[self.NAV_SUBNAV[0], self.NAV_SUBNAV[1].replace('{SUB_STRING}', category)]

#   here we return two things: index 0 (which is in NAV_SUBNAV's By.CSS_SELECTOR)
#   and Index 1 (which is #nav-subnav[data-category='{SUB_STRING}'])
#   in index 1 we replace SUB_STRING by category.
#   Then under def_verify_department_selected(self):
#    locator = self.get_subnav_locator(category)    <--- This will build us a locator
#   self.wait_for_element_appear(*locator)
#   instead of hardcoded "verify books dept selected", we make books dynamic:
#   in search_results_page, def_verify_department_selected(self) will be (self, category)
#   here in steps, books --> {category} and context.app.search_results_page.verify_department_selected() --> (category)


@when('Select department by alias {alias}')
def select_dept(context, alias):
    context.app.header.select_dept(alias)


@then('Verify {category} department is selected')
def verify_dept_is_selected(context, category):
    context.app.search_results_page.verify_dept_is_selected(category)
