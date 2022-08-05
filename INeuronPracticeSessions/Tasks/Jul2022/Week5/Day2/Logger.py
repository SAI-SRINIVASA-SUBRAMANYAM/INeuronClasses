import logging


class LogType:
    Error = 'error'
    Warning = 'warn'
    Info = 'info'


class Logger(LogType):

    def __init__(self, message: str, log_type: str = LogType.Info):
        """
        Custom logging mechanism, with static file and format.\n
        Log types are of I: Information, W: Warning, E: Error. Other types as Warning
        :param log_type: str
        """
        logging.basicConfig(filename="app.log",
                            level=logging.DEBUG,
                            format="%(asctime)s %(name)s %(levelname)s %(message)s")

        log_message = message if message != "" else "Unknown log message."
        if log_type == LogType.Error:
            logging.error(log_message)
        elif log_type == LogType.Warning:
            logging.warning(log_message)
        else:
            print(log_message)
            logging.info(log_message)