import os.path
import re
import setuptools


def read(relative_path):
    here = os.path.abspath(os.path.dirname(__file__))
    there = os.path.join(here, relative_path)
    with open(there, "r", encoding="utf-8") as fh:
        return fh.read()


def get_version(relative_path):
    text = read(relative_path)
    match = re.findall(r"__version__ = \"(.+)\"", text)
    try:
        return match[0]
    except IndexError:
        raise RuntimeError("Failed to find version string.")


setuptools.setup(
    name="nitsm",
    version=get_version("src/nitsm/__init__.py"),
    author="NI",
    author_email="opensource@ni.com",
    description="NI TestStand Semiconductor Module Python API",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/ni/nitsm-python",
    package_dir={"": "src"},  # sets package root to the src directory
    packages=setuptools.find_packages("src", include=("nitsm",)),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6",
    install_requires=["pywin32>=228;platform_system=='Windows'"],
)
