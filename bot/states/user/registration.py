from aiogram.fsm.state import State, StatesGroup

class RegistrationState(StatesGroup):
    name = State()
    age = State()
    gender = State()
    specialization = State()