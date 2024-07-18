import logging
logger=logging.getLogger("logging_name")
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s', datefmt='%m-%Y-%d %H:%M:%S')
def main():
  logger.debug("this is a debu g message")
  logger.info("this is a info message")
  logger.warning("this is a warning level message")
  logger.error("\033[94mthis is a error level message\033[0m")
if __name__=="__main__":
  main()