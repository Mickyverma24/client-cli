from setuptools import setup, find_packages

setup(
    name='pmclient',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["main"], 
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        'console_scripts': [
            'pmclient=main:cli',  
        ],
    },
)