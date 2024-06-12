from pathlib import Path
from selene import browser, have
import tests_demoga


class RegistrationPage:
    def __init__(self):
        self.subject = browser.element("#subjectsInput")

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def choice_gender(self):
        browser.element('[for="gender-radio-1"]').click()


