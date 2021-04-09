from setuptools import setup

setup(
    name="prodas",
    version="0.0.1dev1",
    description="Programming Data Science",
    author="Philipp",
    packages=["prodas"],
    entry_point={
        'console_scripts': ['prodas_cli=prodas.cli:main']
    }
)
