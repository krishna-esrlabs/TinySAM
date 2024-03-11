from setuptools import find_packages, setup

setup(
    name="tinysam",
    version="1.0",
    install_requires=[],
    packages=find_packages(),
    extras_require={
        "all": ["matplotlib"],
    },
)
