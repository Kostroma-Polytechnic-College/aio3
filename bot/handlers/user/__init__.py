from aiogram import Dispatcher

from . import registration

def include_routers(dp: Dispatcher):
    dp.include_routers(
        registration.router
    )