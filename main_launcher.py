import traceback

from src.api.start_services import start_services

def main():
    try:
        print("Launcher started")
        start_services()
    except Exception as e:
        print("ERROR:")
        traceback.print_exc()
        input("Press enter to exit...")

if __name__ == "__main__":
    main()