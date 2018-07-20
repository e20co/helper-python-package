from setuptools import setup, find_packages

setup(
    name='helper',

    version='0.1',

    description='Configuration Manager',
    classifiers=[
        'Development Status :: 5 - Alpha'
    ],
    keywords='helper, type checking, retry',
    package_dir={'': 'helper_python'},
    packages=find_packages('helper')
)
