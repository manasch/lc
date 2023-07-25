from setuptools import find_packages, setup

setup(
    name="lc",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "lc = src.lc:main"
        ]
    },
    install_requires=[
        "fire",
        "requests"
    ]    
)
