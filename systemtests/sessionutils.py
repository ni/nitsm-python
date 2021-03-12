import re


def get_resource_name_from_session(session) -> str:
    """
    session.io_resource_descriptor isn't 100% reliable for simulated sessions. This method uses a
    regular expression to get the resource name from the object's repr.
    """

    return re.search(r"resource_name='(\w*)'", repr(session)).group(1)
