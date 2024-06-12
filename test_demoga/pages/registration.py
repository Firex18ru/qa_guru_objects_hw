from pathlib import Path
from selene import browser, have
from data.user import User

class RegistrationPage:

    def __init__(self):
        self.state = browser.element('#state')
        self.city = browser.element('#city')
    def open(self):
        browser.open("/automation-practice-form")

    def _fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def _fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def _fill_email(self, value):
        browser.element("#userEmail").type(value)

    def _choice_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def _fill_phone_number(self, value):
        browser.element("#userNumber").type(value)

    def _fill_birthday(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(f".react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)").click()

    def _choice_subject(self, value):
        browser.element("#subjectsInput").type(value).press_enter()

    def _choice_hobbies(self):
        browser.element("[for = hobbies-checkbox-1]").click()
        browser.element("[for = hobbies-checkbox-2]").click()

    def _upload_picture(self, file):
        browser.element("#uploadPicture").type(str(Path(__file__).parent.parent.joinpath(f"resources/", file)))

    def _fill_adress(self, value):
        browser.element("#currentAddress").type(value)

    def _choice_state(self):
        browser.element("#state").click().element("#react-select-3-option-0").click()

    def _choice_city(self):
        browser.element("#city").click().element("#react-select-4-option-0").click()

    def _submit(self):
        browser.element("#submit").click()

    def register(self, student: User):
        (
            self._fill_first_name(student.name)
            ._fill_last_name(student.surname)
            ._fill_email(student.email)
            ._choice_gender(student.gender)
            ._fill_phone_number(student.phone)
            ._fill_date_of_birth(
                student.date_year, student.date_month, student.date_day
            )
            ._fill_subjects(student.subject)
            ._fill_hobbies(student.hobby)
            ._upload_picture(student.photo)
            ._fill_address(student.address)
            ._fill_state(student.state)
            ._fill_city(student.city)
            ._submit()
        )

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
