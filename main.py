from cli.commands import get_args


def start_app(config_file):
    print("Starting automation tool...")
    if config_file:
        print(f"Using config file: {config_file}")
    else:
        print("No config file given yet.")


def stop_app():
    print("Stop requested.")
    print("For now, press Ctrl+C if the app is running.")


def show_status():
    print("Status: automation tool CLI is working.")


def main():
    args = get_args()

    if args.command == "start":
        start_app(args.config)
    elif args.command == "stop":
        stop_app()
    elif args.command == "status":
        show_status()


if __name__ == "__main__":
    main()