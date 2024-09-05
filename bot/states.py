from telebot.states import State, StatesGroup

class LegalRegisterState(StatesGroup):
    COMPANY_NAME = State()
    EMPLOYEE_NAME = State()
    COMPANY_CONTACT = State()
    EMPLOYEE_COUNT = State()
    DURATION_DAYS = State()
    WORKING_DAYS = State()

class IndividualRegisterState(StatesGroup):
    NAME = State()
    CONTACT = State()