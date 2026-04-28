import logging
from src.setup.run_gui import run_gui
from src.setup.run_setup import run_setup
from src.utils.setup_logging import setup_logging, setup_uvicorn_logging

# Start Logging
setup_logging("setup.log", level=logging.DEBUG)

def pipeline(domain, log=None):
    return run_setup(domain, log=log)


def main():
    run_gui(pipeline)


if __name__ == "__main__":
    main()