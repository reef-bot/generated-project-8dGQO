import logging

class Logger:
    def __init__(self):
        logging.basicConfig(filename='bot.log', level=logging.INFO)

    def log_action(self, action):
        logging.info(action)