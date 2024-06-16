from pathlib import Path
from selene import browser, have


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    def choice_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def fill_phone_number(self, value):
        browser.element("#userNumber").type(value)

    def fill_birthday(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(f".react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)").click()

    def choice_subject(self, value):
        browser.element("#subjectsInput").type(value).press_enter()

    def choice_hobbies(self):
        browser.element("[for = hobbies-checkbox-1]").click()
        browser.element("[for = hobbies-checkbox-2]").click()

    def upload_picture(self, file):
        browser.element("#uploadPicture").type(str(Path(__file__).parent.parent.joinpath(f"resources/", file)))

    def fill_adress(self, value):
        browser.element("#currentAddress").type(value)

    def choice_state(self):
        browser.element("#state").click().element("#react-select-3-option-0").click()

    def choice_city(self):
        browser.element("#city").click().element("#react-select-4-option-0").click()

    def submit(self):
        browser.element("#submit").click()

    def should_user(self, full_name, email, gender, number, date, subjects, hobbies, file, address, state):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                date,
                subjects,
                hobbies,
                file,
                address,
                state
            )
        )
