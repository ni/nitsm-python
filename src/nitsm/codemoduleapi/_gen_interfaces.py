import sys
from win32com.client import makepy

outputfile = r"C:\Users\Public\Documents\pinmapinterfaces.py"

comType = (
    r"C:\Program Files\National Instruments\TestStand 2020\Bin"
    r"\NationalInstruments.TestStand.SemiconductorModule.PinMapInterfaces.tlb"
)

sys.argv = ["makepy", "-o", outputfile, comType]

if __name__ == "__main__":
    makepy.main()
