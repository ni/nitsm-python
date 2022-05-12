import sys
import os.path
import winreg
from win32com.client import makepy


def get_env_variable_from_registry(variable_name):
    key = winreg.CreateKey(
        winreg.HKEY_LOCAL_MACHINE, r"System\CurrentControlSet\Control\Session Manager\Environment"
    )
    return winreg.QueryValueEx(key, variable_name)[0]


output_file = os.path.join(os.path.dirname(__file__), "_pinmapinterfaces.py")
_teststand_public_path = get_env_variable_from_registry("TestStandPublic64")
pmi_type_library = os.path.join(
    _teststand_public_path,
    "Bin",
    "NationalInstruments.TestStand.SemiconductorModule.PinMapInterfaces.tlb",
)

sys.argv = ["makepy", "-o", output_file, pmi_type_library]

if __name__ == "__main__":
    makepy.main()
