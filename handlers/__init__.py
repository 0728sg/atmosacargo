from .sync import sync_command

def register_handlers(dp):
    dp.register_message_handler(sync_command, commands=["sync"])

