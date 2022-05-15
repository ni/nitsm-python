"""Generates _pinmapinterfaces.py

You must register the correct version of TSM with TestStand Version Selector prior to running this
script.
"""

import sys
import os.path
from win32com.client import makepy

output_file = os.path.join(os.path.dirname(__file__), "_pinmapinterfaces.py")
teststand_public_path = os.environ["TestStandPublic64"]
pmi_type_library = os.path.join(
    teststand_public_path,
    "Bin",
    "NationalInstruments.TestStand.SemiconductorModule.PinMapInterfaces.tlb",
)

sys.argv = ["makepy", "-o", output_file, pmi_type_library]

if __name__ == "__main__":
    makepy.main()
