#!/usr/bin/env python3
import shutil
from setuptools import find_packages, setup

with open("README.txt") as f:
    readme = f.read()

shutil.copy("cppcheck-htmlreport", "cppcheck_htmlreport/run.py")

setup(
    name="cppcheck-htmlreport",
    description=(
        "Python script to parse the XML (version 2) output of "
        "cppcheck and generate an HTML report using Pygments for syntax "
        "highlighting."
    ),
    long_description=readme,
    author="Henrik Nilsson",
    url="https://github.com/danmar/cppcheck",
    license="GPL",
    packages=find_packages(exclude=("tests", "docs")),
    use_scm_version={"root": ".."},
    entry_points={
        "console_scripts": [
            "cppcheck-htmlreport = cppcheck_htmlreport:run.main",
        ]
    },
    test_suite="tests",
    install_requires=["Pygments"],
    setup_requires=["setuptools>=60", "setuptools-scm>=8.0"],
)
