"""Configuration and dependencies for the Data Entry Clerk."""
from setuptools import setup

setup(
    name='data-entry-clerk',
    version='0.1',
    description='Simple server to store incoming webhooks in a database',
    url='http://github.com/automatiqa/data-entry-clerk',
    author='Automatiqa',
    license='MIT',
    packages=['dec'],
    include_package_data=True,
    install_requires=[
        'boto3',
        'flask',
        'pytz',
        'simplejson'
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest'
    ]
)
