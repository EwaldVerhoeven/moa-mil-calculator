from setuptools import find_namespace_packages, setup

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='moa-mil-calculator',
    version='0.0.1',
    description='zero your scope quickly and correct!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_namespace_packages(
        include=['src', 'src.*']
    ),
    install_requires=[
        'measurement==3.2.0',
        'matplotlib==3.6.0',
        'opencv-python==4.6.0.66',
        'numpy==1.23.0'
    ],
    extras_require={
        'dev': [
            'pytest==7.1.3',
            'pytest-reporter==0.5.2',
            'pytest-reporter-html1==0.8.2',
            'pytest-asyncio==0.19.0',
            'flake8==5.0.4',
            'pre-commit==2.20.0'
            ]
    }
)
