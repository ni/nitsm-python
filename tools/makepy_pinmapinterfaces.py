import sys
import os.path
from win32com.client import makepy

output_file = os.path.join(os.path.dirname(__file__), "_pinmapinterfaces.py")
pmi_type_library = (
    r"C:\Program Files\National Instruments\TestStand 2020\Bin"
    r"\NationalInstruments.TestStand.SemiconductorModule.PinMapInterfaces.tlb"
)

sys.argv = ["makepy", "-o", output_file, pmi_type_library]

if __name__ == "__main__":
    makepy.main()
