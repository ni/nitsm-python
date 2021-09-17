import re


def get_resource_name_from_session(session) -> str:
    """
    session.io_resource_descriptor isn't 100% reliable for simulated sessions. This method uses a
    regular expression to get the resource name from the object's repr.
    """

    return re.search(r"resource_name='(\w*)'", repr(session)).group(1)


def get_task_name_from_task(task) -> str:
    """Uses a regular expression on the task's repr to return the task's name."""
    return re.search(r"Task\(name=(\w*)\)", repr(task)).group(1)
