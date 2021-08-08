"""
Use this code snippet to pause the Python interpreter and display the process ID (PID). The PID
can be used by an IDE such as PyCharm to attach to the process for debugging. This is useful for
stepping into Python TSM code modules from TestStand.

Instructions for use from PyCharm:
1. Copy the code snippet below into the code module you want to debug. Placing it at the beginning
    of the code module is recommended.
2. Add a breakpoint at the location where you want to start debugging. Make sure this breakpoint is
    after the MessageBoxW function.
3. Execute the sequence that calls into the code module from TestStand.
4. A dialog box will appear displaying the PID of the current process. Before clicking "Okay" on the
    dialog, select Run -> Attach To Process... from the PyCharm menu.
5. PyCharm will display a window of discovered processes. Click the process with the matching PID.
6. PyCharm will open a debug terminal and attach to the TestStand process. Once PyCharm is attached,
    click "Okay" on the dialog to continue execution. If the steps were performed correctly, PyCharm
    will break at the first breakpoint it reaches in the code.
"""

import os
import ctypes

ctypes.windll.user32.MessageBoxW(
    None, "Process name: niPythonHost.exe and Process ID: " + str(os.getpid()), "Attach debugger", 0
)
