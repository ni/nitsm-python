[![Build Status](https://ni.visualstudio.com/DevCentral/_apis/build/status/TSM/nitsm-python-tests?branchName=main)](https://ni.visualstudio.com/DevCentral/_build/latest?definitionId=5945&branchName=main)
# nitsm-python
Write code modules with the TestStand Semiconductor Module in python.

## Note to End Users
This project is not intended for use in a production environment. Our primary focus is to provide a pythonic approach to
automated testing with TestStand and TSM. More emphasis has been placed on simplicity and usability than execution time.

## Python Version Support
nitsm supports python versions 3.6, 3.7, and 3.8. Newer versions of python might work, but it is not guaranteed. Python
2.7 is not supported.

## Installation
```
pip install nitsm
```

nitsm requires [NI TestStand](https://www.ni.com/en-us/support/downloads/software-products/download.teststand.html)
20.0 or higher and
[NI TestStand Semiconductor Module](https://www.ni.com/en-us/support/downloads/software-products/download.teststand-semiconductor-module.html)
20.0 or higher.

To use nitsm in conjunction with [nimi-python](https://github.com/ni/nimi-python), you must also install the appropriate
NI instrument driver for each device you plan to use:
  - [NI-DCPower](https://www.ni.com/en-us/support/downloads/drivers/download.ni-dcpower.html)
  - [NI-DMM](https://www.ni.com/en-us/support/downloads/drivers/download.ni-dmm.html)
  - [NI-SCOPE](https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html)
  - [NI-Digital](https://www.ni.com/en-us/support/downloads/drivers/download.ni-digital-pattern-driver.html)
  - [NI-SWITCH](https://www.ni.com/en-us/support/downloads/drivers/download.ni-switch.html)
  - [NI-DAQmx](https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html)
  - [NI-FGEN](https://www.ni.com/en-us/support/downloads/drivers/download.ni-fgen.html)

Visit the [nimi-python](https://github.com/ni/nimi-python) project for information on which python packages to install
alongside each instrument driver.

## Usage
Define code modules with the `code_module` decorator in the `nitsm.codemoduleapi` module. When called from TestStand,
the decorator will convert the [pywin32](https://pypi.org/project/pywin32/) COM object into an
`nitsm.codemoduleapi.SemiconductorModuleContext` object.

```python
import nidcpower
import nitsm.codemoduleapi

@nitsm.codemoduleapi.code_module
def source_current(tsm_context, pins, current_level):
    pin_query_context, sessions, channel_strings = tsm_context.pins_to_nidcpower_sessions(pins)
    for session, channel_string in zip(sessions, channel_strings):
        session.channels[channel_string].output_function = nidcpower.OutputFunction.DC_CURRENT
        session.channels[channel_string].current_level = current_level
        session.channels[channel_string].initiate()
```

## Known Limitations
* Instrument alarms are currently not supported
* The Set Relays TestStand step is not supported when creating relay sessions in python 
* See [STATUS.md](https://github.com/ni/nitsm-python/blob/main/STATUS.md) for additional information about the current 
state of the API and system tests
