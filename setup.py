from setuptools import setup, find_packages

setup(
    name='helper',

    version='0.1',

    description='Helper Python',
    classifiers=[
        'Development Status :: 5 - Alpha'
    ],
    keywords='helper, type checking, retry',
    package_dir={'': 'helper'},
    packages=find_packages('helper')
)
