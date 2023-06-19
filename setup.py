from setuptools import find_packages, setup

DEPENDENCIES = []

setup(
    name="cwh",
    version="0.0.1",
    install_requires=[
        "requests >= 2.31.0", "fire >= 0.5.0"
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cwh = src.__main__:main"
        ]
    }
)
