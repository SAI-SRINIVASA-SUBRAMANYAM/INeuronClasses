from Tasks.Jul2022.Jul07Task.Utils.CustomLogging import CLogger


class CExcept(CLogger):
    """
    Custom exception handling with overlay wrapper.
    """
    def __init__(self, message: str):
        error_message = message if message.strip() != "" else "Unknown Error"
        CLogger(error_message, 'e')
        raise Exception(error_message)

