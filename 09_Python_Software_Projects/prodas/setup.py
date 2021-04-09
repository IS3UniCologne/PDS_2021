from setuptools import setup

setup(
    name="prodas",
    version="0.0.1dev1",
    description="Programming Data Science",
    author="Philipp",
    packages=["prodas"],
    entry_points={
        'console_scripts': [
            'prodas = prodas.cli:main'
        ]
    }
)
