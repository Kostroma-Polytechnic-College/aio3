from aiogram import Dispatcher

from . import commands
from . import user

def include_routers(dp: Dispatcher):
    
    user.include_routers(dp)
    
    dp.include_routers(
        commands.router
    )