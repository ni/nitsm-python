[![Build Status](https://ni.visualstudio.com/Users/_apis/build/status/nitsm-python?branchName=main)](https://ni.visualstudio.com/Users/_build/latest?definitionId=5837&branchName=main)
# nitsm-python

## Tests
### Dependencies
Before you can run tests you must install the following:
* [TestStand 20.0+](https://www.ni.com/en-us/support/downloads/software-products/download.teststand.html)
* [TestStand Semiconductor Module 20.0+](https://www.ni.com/en-us/support/downloads/software-products/download.teststand-semiconductor-module.html)
* TSM standalone context
    * Copy locally from \\nirvana\perforceexports\TesterOS\TSM\StandaloneSemiconductorModuleContext
    * Execute RegisterAssembly.bat as administrator (see Readme.txt)
* NI drivers:
  - [NI-DCPower](https://www.ni.com/en-us/support/downloads/drivers/download.ni-dcpower.html)
  - [NI-DMM](https://www.ni.com/en-us/support/downloads/drivers/download.ni-dmm.html)
  - [NI-SCOPE](https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html)
  - [NI-Digital](https://www.ni.com/en-us/support/downloads/drivers/download.ni-digital-pattern-driver.html)
  - [NI-SWITCH](https://www.ni.com/en-us/support/downloads/drivers/download.ni-switch.html)
  - [NI-DAQmx](https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html)
  - [NI-FGEN](https://www.ni.com/en-us/support/downloads/drivers/download.ni-fgen.html)
* NI python bindings:
```
pip install nidcpower nidmm niscope nidigital niswitch nidaqmx nifgen
```
* Pytest 
```
pip install pytest
```
* Python for Win32 extensions
```
pip install pywin32
```
After installing the required dependencies, install nitsm in edit mode then run pytest.
```
pip install -e .
pytest
```
