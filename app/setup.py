from setuptools import find_namespace_packages, setup

# with open('README.md', 'r') as readme:
#     long_description = readme.read()

setup(
    name='moa-mil-calculator',
    version='0.0.1',
    description='zero your scope quickly and correct!',
    long_description="test",
    long_description_content_type='text/markdown',
    # py_modules=[],
    # package_dir={'': 'app'},
    packages=find_namespace_packages(
        include=['src', 'src.*']
    ),
    install_requires=[
        'measurement==3.2.0',
        'matplotlib==3.6.0'
    ],
    extras_require={
        'dev': [
            'pytest==7.1.3',
            'pytest-reporter==0.5.2',
            'pytest-reporter-html1==0.8.2',
            'pytest-asyncio==0.19.0',
            'flake8==5.0.4'
            ]
    }
)
