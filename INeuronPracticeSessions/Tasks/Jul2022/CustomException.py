from CustomLogging import Logger


class CExcept:
    def __init__(self, message):
        Logger(message, 'e')
        raise Exception(message)
