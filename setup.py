import setuptools

from src.testproject import definitions

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testproject-python-sdk",
    version=definitions.get_sdk_version(),
    author="TestProject",
    author_email="contact@testproject.io",
    description="Selenium and Appium powered SDK for TestProject.io",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://testproject.io/selenium-appium-powered-sdk/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.4",
    install_requires=[
        "selenium==3.141.0",
        "Appium-Python-Client==1.0.1",
        "decorator>=4.4.2",
        "requests>=2.24.0",
    ],
)
