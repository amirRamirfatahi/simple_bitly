from setuptools import setup, find_packages

install_requires = []

setup(
    name='simple_bitly',
    version='0.1dev',
    description='Url shortener wsgi application',
    long_description=open('README.md').read(),
    install_requires=install_requires,
    packages=find_packages()
)

