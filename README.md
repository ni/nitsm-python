# nitsm-python

## Tests

Before you can run tests you must install the following:
* Python for Win32 extensions (pip install pywin32)
* TestStand
* TestStand Semiconductor Module
* TSM standalone context
    * copy locally from \\nirvana\perforceexports\TesterOS\TSM\StandaloneSemiconductorModuleContext
    * execute RegisterAssembly.bat as administrator (see Readme.txt)
* NI drivers: NI-DCPower, NI-DMM, NI-SCOPE, NI-Digital, NI-SWITCH, NI-DAQmx, NIFGEN
* NI drivers python API (use pip install <package> for the following packages): nidcpower, nidmm, niscope, nidigital, niswitch, nidaqmx, nifgen

To run pytest from the command line, install nitsm in edit mode then run pytest.
```
pip install -e .
pytest
```
