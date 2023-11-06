import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

# x = 4
# logging.info(f"The value for x is {x}")

try:
    1 / 0
except ZeroDivisionError as e:
    #logging.error("ZeroDivError", exc_info=True)
    logging.exception("ZeroDivError")

logger = logging.getLogger(__name__) #we conventially use __name__ cause we create logger for each module
handler=logging.FileHandler("test.log")
handler.setLevel(logging.INFO)
formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


logger.info("Test the custom logger")