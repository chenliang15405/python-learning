"""
将日志输出到控制台

"""
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.debug("这是debug logging....")
logging.info("这是info logging....")
logging.warning("这是warning logging....")
logging.error("这是error logging....")
logging.critical("这是critical logging....")
