import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nitsm",
    version="0.1.0a0",
    author="NI",
    author_email="opensource@ni.com",
    description="NI TestStand Semiconductor Module Python API",
    long_description=long_description,
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
