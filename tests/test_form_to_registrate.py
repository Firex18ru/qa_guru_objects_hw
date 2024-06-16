from tests_demoga.pages.registration_page import RegistrationPage


def test_form_to_registrate():
    page = RegistrationPage()
    page.open()
    page.fill_first_name("Ivan")
    page.fill_last_name("Yakimenko")
    page.fill_email("Def11@def.ru")
    page.choice_gender()
    page.fill_phone_number("0999777601")
    page.fill_birthday("1989", "February", "11")
    page.choice_subject("Computer Science")
    page.choice_hobbies()
    page.upload_picture("094745.png")
    page.fill_adress("Izhevsk")
    page.choice_state()
    page.choice_city()
    page.submit()
    page.should_user(
        "Ivan Yakimenko",
        "Def11@def.ru",
        "Male",
        "0999777601",
        "11 February,1989",
        "Computer Science",
        "Sports, Reading",
        "094745.png",
        "Izhevsk",
        "NCR Delhi")
