from setuptools import setup, find_packages

setup(
    name="pmi",
    version="0.1",
    packages=find_packages(),  # include your whole codebase
    include_package_data=True,
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "pmi = main:app",  # <package>.<file>:<typer app>
        ],
    },
)
