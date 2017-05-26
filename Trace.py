import logging


class Trace(object):


    @classmethod
    def initLogFile(cls):
        logging.basicConfig(filename='Spicer.log', format="%(asctime)s - %(thread)d - %(levelname)s - %(message)s",level=logging.DEBUG)

    @classmethod
    def Debug(cls, msg, *args, **kwargs):
        logging.debug(msg, *args, **kwargs)

    @classmethod
    def Info(cls, msg, *args, **kwargs):
        logging.info(msg, *args, **kwargs)

    @classmethod
    def War(cls, msg, *args, **kwargs):
        logging.warning(msg, *args, **kwargs)

    @classmethod
    def Error(cls, msg, *args, **kwargs):
        logging.warning(msg, *args, **kwargs)

