import logging

def run_task(task):
    try:
        logging.info("Running: %s", task.task_name)
        task.execute()
        logging.info("Done: %s", task.task_name)
    except Exception as error:
        logging.error("Task failed: %s", error)