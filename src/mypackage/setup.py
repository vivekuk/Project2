from setuptools import setup, find_packages

setup(
    name='your_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'matplotlib',
        'seaborn',
        'lxml',
    ],
)
