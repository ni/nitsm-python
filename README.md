[![Build Status](https://ni.visualstudio.com/DevCentral/_apis/build/status/TSM/nitsm-python-tests?branchName=main)](https://ni.visualstudio.com/DevCentral/_build/latest?definitionId=5945&branchName=main)
# nitsm-python
## Installation
`pip install nitsm`
## Known Limitations
* Instrument alarms are currently not supported
* See [STATUS.md](./STATUS.md) for additional information about the current state of the API and system tests
## Tests
Executing the nitsm-python tests requires the **TSM Standalone Semiconductor Module Context**. If you are not an
NI employee, contact one of the
repository owners to determine how to obtain a copy of this non-public component.

Before you can run tests you must install the following:
* [TestStand 20.0+](https://www.ni.com/en-us/support/downloads/software-products/download.teststand.html)
* [TestStand Semiconductor Module 20.0+](https://www.ni.com/en-us/support/downloads/software-products/download.teststand-semiconductor-module.html)
* TSM standalone context
    * Copy locally from \\\nirvana\perforceexports\TesterOS\TSM\StandaloneSemiconductorModuleContext
    * Execute RegisterAssembly.bat as administrator (see Readme.txt)
* NI drivers:
  - [NI-DCPower](https://www.ni.com/en-us/support/downloads/drivers/download.ni-dcpower.html)
  - [NI-DMM](https://www.ni.com/en-us/support/downloads/drivers/download.ni-dmm.html)
  - [NI-SCOPE](https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html)
  - [NI-Digital](https://www.ni.com/en-us/support/downloads/drivers/download.ni-digital-pattern-driver.html)
  - [NI-SWITCH](https://www.ni.com/en-us/support/downloads/drivers/download.ni-switch.html)
  - [NI-DAQmx](https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html)
  - [NI-FGEN](https://www.ni.com/en-us/support/downloads/drivers/download.ni-fgen.html)
* Python packages:
```
pip install -r requirements.txt
```
After installing the required dependencies, install nitsm in edit mode then run pytest.
```
pip install -e .
pytest
```
