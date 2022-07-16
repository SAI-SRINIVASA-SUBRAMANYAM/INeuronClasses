import logging


class CLogger:
    def __init__(self, message: str, log_type: str='w'):
        """
        Custom logging mechanism, with static file and format.\n
        Log types are of I: Information, W: Warning, E: Error. Other types as Warning
        :param log_type: str
        """
        logging.basicConfig(filename="app.log",
                            level=logging.DEBUG,
                            format="%(asctime)s %(name)s %(levelname)s %(message)s")

        log_message = message if message != "" else "Unknown log message."
        c_log_type = log_type[0] if len(log_type) > 1 else log_type
        if c_log_type.lower() == "e":
            logging.error(log_message)
        elif c_log_type.lower() == "i":
            print(log_message)
            logging.info(log_message)
        else:
            logging.warning(log_message)

