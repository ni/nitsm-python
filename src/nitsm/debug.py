import os
import tkinter.messagebox


def prompt_attach_debugger() -> None:
    """
    Pauses the Python interpreter and displays the process ID (PID). The PID can be used by an IDE
    such as PyCharm to attach to the process for debugging. This is useful for stepping into nitsm
    code modules from TestStand.

    Instructions for use with PyCharm:
        1. Call this function from the code module you want to debug. Placing it at the beginning
            of the code module is recommended.
        2. Add a breakpoint at the location where you want to start debugging. Make sure this
            breakpoint will be reached after this function is called.
        3. In TestStand, execute a sequence that calls into the code module.
        4. A dialog box will appear displaying the PID of the current process. Before clicking
            "Okay" on the dialog, select Run -> Attach To Process... from the PyCharm menu.
        5. PyCharm will display a window of discovered processes. Click the process with the
            matching PID.
        6. PyCharm will open a debug terminal and attach to the process. Wait for PyCharm to
            indicate it has successfully attached.
        6. Once PyCharm is attached, click "Okay" on the dialog to continue execution. If these
            steps were performed correctly, PyCharm will break at the first breakpoint it reaches in
            the code.
    """

    tkinter.Tk().withdraw()  # hide root window
    tkinter.messagebox.showinfo(
        "Attach debugger", "Process name: niPythonHost.exe and Process ID: " + str(os.getpid())
    )
    return


if __name__ == "__main__":
    prompt_attach_debugger()
