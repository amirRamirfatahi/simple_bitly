from setuptools import setup, find_packages

dependencies = [
    'yhttp',
    'redis',
    'hashids'
]

setup(
    name='simple_bitly',
    version='0.1',
    description='Url shortener wsgi application',
    long_description=open('README.md').read(),
    install_requires=dependencies,
    packages=find_packages(),
    license='MIT'
)
