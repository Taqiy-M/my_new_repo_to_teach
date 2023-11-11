from aiogram.dispatcher.filters.state import StatesGroup, State

class Holatlarim(StatesGroup):
    kontaktState = State()
    locationState = State()
    mainState = State()
    menuState = State()
    sozlamarState = State()


class AdminUchun(StatesGroup):
    nom = State()
    rasm = State()
    descr = State()
