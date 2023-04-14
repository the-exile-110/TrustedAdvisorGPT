import logging
from rich.logging import RichHandler

logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])


def lambda_handler(event, context):
    logging.info("Hello World")


if __name__ == "__main__":
    lambda_handler(None, None)
