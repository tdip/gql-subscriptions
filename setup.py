import sys
from setuptools import setup, find_packages

setup(
    name='gql-async',
    version='0.1.0',
    description='GraphQL client for Python',
    long_description=open('README.rst').read(),
    url='https://github.com/tdip/gql-subscriptions',
    author='Turning Data Into Products A.S.',
    author_email='hello@quantifio.no',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='api graphql subscription',
    packages=find_packages(include=["gql_async*"]),
    install_requires=[
    ],
    tests_require=['pytest>=2.7.2', 'mock'],
)
