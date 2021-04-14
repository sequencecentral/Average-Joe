from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='averagejoe',
    packages=['averagejoe'],
    description='averagejoe',
    url='https://github.com/sequencecentral/averagejoe.git',
    # git+https://github.com/sequencecentral/averagejoe.git@main#egg=averagejoe
    author='Steve Ayers',
    author_email='steve@sequenccecentral.com',
    install_requires=[],
    version='1.0',
    license='',
    long_description=open('README.md').read(),
)
