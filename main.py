import sys
from cli.commands import get_args
from config.config_loader import check_config, load_config

def list_tasks(config_file):
    config = load_config(config_file)
    check_config(config)
    print("Tasks:")
    for task in config["tasks"]:
        print(f"- {task['task_name']} ({task['task_type']})")

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
    try:
        if args.command == "start":
            start_app(args.config)
        elif args.command == "list":
            list_tasks(args.config)
        elif args.command == "stop":
            stop_app()
        elif args.command == "status":
            show_status()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()