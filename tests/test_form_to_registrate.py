from selene import browser
from tests_demoga.pages.registration import RegistrationPage


def test_form_to_registrate():
    page = RegistrationPage()
    (
        page.open()
        .fill_first_name("Ivan")
        .fill_last_name("Yakimenko")
        .fill_email("Def11@def.ru")
        .choice_gender("Male")
        .fill_phone_number("0999777601")
        .fill_birthday("01", "February", "1989")
        .choice_subject("Computer Science")
        .choice_hobbies("Sports, Reading")
        .upload_picture("094745.png")
        .fill_adress("Izhevsk")
        .choice_state()
        .choice_city()
        .submit()
        .should_user(
            "Ivan Yakimenko",
            "Def11@def.ru",
            "Male",
            "0999777601",
            "01 February,1989",
            "Computer Science",
            "Sports, Reading",
            "094745.png",
            "Izhevsk",
            "NCR Delhi")

    )



    browser.element("#closeLargeModal").click()