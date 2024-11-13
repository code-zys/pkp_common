from setuptools import setup, find_packages

setup(
    name='pkp_common',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'mongoengine',
        'tzlocal',
        'pytz',
        'boto3',
        'blinker',
        'pydantic',
        'pydantic-settings',
        'python-jose',
        'imap_tools',
        'requests'
    ],
    description='Pocker Planning  common module',
    author='Cedric',
    url='https://github.com/code-zys/pkp_common',
)
