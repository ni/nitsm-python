import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nitsm",
    version="0.0.1",
    author="NI",
    authoremail="opensource@ni.com",
    description="NI TestStand Semiconductor Module Python API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ni/nitsm-python",
    packages=["src/nitsm"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"
    ],
    python_requires=">=3.6"
)
