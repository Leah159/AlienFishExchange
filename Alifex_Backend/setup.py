"""
Setup file for installing project requirements
"""

# Built-in
from setuptools import find_packages, setup

NAME = "Alien Fish Exchange"
VERSION = "0.0.2"
REQUIREMENTS = ["bcrypt", "flask", "flask_cors", "jsonschema", "pyjwt", "requests", "vulture"]
EXTRA_REQUIREMENTS = {"test": ["pylint", "pytest==6.2.4"]}
DESCRIPTION = "Alien Fish Exchange"
setup(
    name="Alien Fish Exchange",
    version="0.0.1",
    install_requires=REQUIREMENTS,
    extras_require=EXTRA_REQUIREMENTS,
    include_package_data=True,
    requires=REQUIREMENTS,
    packages=find_packages(),
    test_suite="pytest",
    description=DESCRIPTION,
)
