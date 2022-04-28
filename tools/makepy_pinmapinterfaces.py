"""Generates _pinmapinterfaces.py

You must register the correct version of TSM with TestStand Version Selector prior to running this
script.
"""

import sys
import os.path
from win32com.client import makepy

output_file = os.path.join(os.path.dirname(__file__), "_pinmapinterfaces.py")
type_library = "NI TestStand 2020 Semiconductor Module Pin Map Interfaces"
sys.argv = ["makepy", "-o", output_file, type_library]

if __name__ == "__main__":
    makepy.main()
