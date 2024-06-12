from data.user import User
from test_demoga.pages.registration import RegistrationPage


def test_form_to_registrate():
    page = RegistrationPage()
    user = User(
        "Ivan",
        "Yakimenko",
        "Def11@def.ru",
        "Male",
        "0999777601",
        "1989", "February", "11",
        "Computer Science",
        "Sports, Reading",
        "094745.png",
        "Izhevsk",
        "NCR",
        "Delhi"
    )
    page.open().register(user).should_registered_user_with(user)