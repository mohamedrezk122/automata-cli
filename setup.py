#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="automata-cli",
    version="0.1",
    description="A programmatic automata renderer and minimizer",
    author="Mohamed Rezk",
    author_email="mohrizq895@gmail.com",
    url="https://github.com/mohamedrezk122/automata-cli",
    packages=find_packages(),
    py_modules=["automata_cli"],
    include_package_data=True,
    install_requires=["Click", "networkx" ,"graphviz", "pyyaml", "dot2tex"],
    entry_points = """
    [console_scripts]
    automata-cli=automata_cli.automata_cli:cli
    """
)
