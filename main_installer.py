from src.setup.gui import run_gui
from src.setup.setup import run_setup
from src.start_services import start_services

def pipeline(domain):
    try:
        run_setup(domain)
        start_services()

    except Exception as e:
        print(f"Installation Error: {e}")


def main():
    run_gui(pipeline)


if __name__ == "__main__":
    main()