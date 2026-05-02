from setuptools import find_packages
from setuptools import setup

setup (
    name="Adonis",
    version="v0.2.1",
    description="""
`Adonis` is a small Python library for working with ANSI terminal colours.
"""
    author="Jonathon Chew",
    author_email="jonchew626@hotmail.com",
    url="https://github.com/jonathon-chew/Adonis",
    packages=find_packages(exclude=("tests*")),
)
