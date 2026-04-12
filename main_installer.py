from src.setup.run_gui import run_gui
from src.setup.setup import run_setup

def pipeline(domain):
    try:
        run_setup(domain)

    except Exception as e:
        print(f"Installation Error: {e}")


def main():
    run_gui(pipeline)


if __name__ == "__main__":
    main()