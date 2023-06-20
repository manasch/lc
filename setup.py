from setuptools import find_packages, setup

setup(
    name="cwh",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cwh = src.cwh:main"
        ]
    },
    install_requires=[
        "fire",
        "requests"
    ]    
)
