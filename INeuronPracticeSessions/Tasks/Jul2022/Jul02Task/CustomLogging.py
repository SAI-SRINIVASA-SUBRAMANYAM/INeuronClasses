import logging


class Logger:
    def __init__(self, message: str, log_type: str = 'w'):
        """
        Takes text message, log type and file name as arguments.Write log messages at filename and as specified type.\n
        Log type: 'e': Error, 'i': Info, 'w': Warning\n
        :param message: str
        :param log_type: str
        """
        if log_type == "":
            raise Exception("Log type can not be blank")
        elif log_type[0] not in ['e', 'E', 'i', 'I', 'w', 'W']:
            raise Exception("Log type is not valid format")
        elif message == "":
            raise Exception("Log message can not be blank")
        else:
            logging.basicConfig(filename="app.log",
                                level=logging.DEBUG,
                                format="%(asctime)s %(name)s %(levelname)s %(message)s")
            if log_type[0] in ['i', 'I']:
                logging.info(message)
            elif log_type[0] in ['w', 'W']:
                logging.warning(message)
            elif log_type[0] in ['e', 'E']:
                logging.error(message)


