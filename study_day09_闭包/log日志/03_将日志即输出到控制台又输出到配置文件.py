import logging

# 创建logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # log等级总开关

# 第二步 创建一个Handler，用于写入日志文件
logfile = "./log.txt"

fh = logging.FileHandler(logfile, mode="a")  # 表示追加
fh.setLevel(logging.INFO)

# 第三步，再创建一个handler 用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO) # 输出到console的等级

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 将Logger添加到handler里
logger.addHandler(fh)
logger.addHandler(ch)

# 日志
logging.debug("这是debug logging....")
logging.info("这是info logging....")
logging.warning("这是warning logging....")
logging.error("这是error logging....")
logging.critical("这是critical logging....")

