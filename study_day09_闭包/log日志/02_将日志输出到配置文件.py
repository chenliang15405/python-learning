import logging

logging.basicConfig(level=logging.INFO,
                    filename='./log.txt',
                    filemode='a',  # 这里的a表示追加
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.debug("这是debug logging....")
logging.info("这是info logging....")
logging.warning("这是warning logging....")
logging.error("这是error logging....")
logging.critical("这是critical logging....")
