Contributing to nitsm-python
===========================

Contributions to [nitsm-python](https://github.com/ni/nitsm-python) are welcome from all!

nitsm-python is managed via [Git](https://git-scm.com), with the canonical upstream repository hosted on
[GitHub](https://github.com/ni/nitsm-python).

nitsm-python follows a pull request model for development. If you wish to contribute, you will need to create a GitHub
account, fork this project, push a branch with your changes to your project, and then submit a pull request.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for more details.

# Getting Started

## Environment Setup
Before beginning development, it is recommended to install the following dependencies:
* [TestStand 20.0+](https://www.ni.com/en-us/support/downloads/software-products/download.teststand.html)
* [TestStand Semiconductor Module 20.0+](https://www.ni.com/en-us/support/downloads/software-products/download.teststand-semiconductor-module.html)
* NI instrument drivers:
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

## Code Formatting
nitsm-python uses [black](https://black.readthedocs.io/en/stable/index.html) for formatting. To format the entire
project, run:
```
black .
```

## Linting
nitsm-python uses [ni-python-styleguide](https://github.com/ni/python-styleguide) for linting. To lint the entire
project, run:
```
ni-python-styleguide lint
```
**Note:** Only version 1.2 of ni-python-styleguide is currently supported. This issue is tracked by 
[#41](https://github.com/ni/nitsm-python/issues/41).

## Testing
Executing nitsm-python tests in the [tests/](https://github.com/ni/nitsm-python/tree/main/tests) directory requires the
**TSM Standalone Semiconductor Module Context**. If you are an NI employee, contact one of the repository owners to
determine how to obtain a copy of this non-public component. If you are not an NI employee, hang tight! We are currently
working on a process to enable external contributors to use this tool. Note that this does not apply to tests in the
[systemtests/](https://github.com/ni/nitsm-python/tree/main/systemtests) directory.

nitsm uses [pytest](https://docs.pytest.org/) to run tests. First, install nitsm in edit mode:
```
pip install -e .
```
Then, run pytest:
```
pytest
```

Running pytest without arguments will run all tests in the [tests/](https://github.com/ni/nitsm-python/tree/main/tests)
directory. To include system tests, include the [systemtests/](https://github.com/ni/nitsm-python/tree/main/systemtests)
directory.
```
pytest tests systemtests
```

[tox](https://tox.readthedocs.io/en/latest/) is used to run tests against multiple versions of python. To test against
all environments, run:
```
tox
```

The tox configuration in [pyproject.toml](https://github.com/ni/nitsm-python/blob/main/pyproject.toml) creates
environments for running pytest in [tests/](https://github.com/ni/nitsm-python/tree/main/tests) and
[systemtests/](https://github.com/ni/nitsm-python/tree/main/systemtests). It also defines two additional environments,
`clean` and `report` for cleaning and creating report files respectively. To specify a subset of tox environments, run
tox with the `-e` flag followed by a comma separated list of environments:
```
tox -e clean,py36-tests,py36-sysytemtests,report
```

## Building
To build nitsm-python, you will first need to install [build](https://pypi.org/project/build/):
```
pip install build
```
Next, build the project:
```
python -m build
```
If the build succeeds, artifacts will be placed in `dist/`.

# Developer Certificate of Origin (DCO)

   Developer's Certificate of Origin 1.1

   By making a contribution to this project, I certify that:

   (a) The contribution was created in whole or in part by me and I
       have the right to submit it under the open source license
       indicated in the file; or

   (b) The contribution is based upon previous work that, to the best
       of my knowledge, is covered under an appropriate open source
       license and I have the right under that license to submit that
       work with modifications, whether created in whole or in part
       by me, under the same open source license (unless I am
       permitted to submit under a different license), as indicated
       in the file; or

   (c) The contribution was provided directly to me by some other
       person who certified (a), (b) or (c) and I have not modified
       it.

   (d) I understand and agree that this project and the contribution
       are public and that a record of the contribution (including all
       personal information I submit with it, including my sign-off) is
       maintained indefinitely and may be redistributed consistent with
       this project or the open source license(s) involved.

(taken from [developercertificate.org](https://developercertificate.org/))

See [LICENSE](https://github.com/ni/nitsm-python/blob/master/LICENSE) for details about how
[nitsm-python](https://github.com/ni/nitsm-python) is licensed.
