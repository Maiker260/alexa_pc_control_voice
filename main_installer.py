from src.setup.run_gui import run_gui
from src.setup.run_setup import run_setup

def pipeline(domain, log=None):
    return run_setup(domain, log=log)


def main():
    run_gui(pipeline)


if __name__ == "__main__":
    main()