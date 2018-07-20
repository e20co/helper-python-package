from setuptools import setup, find_packages

setup(
    name='helper',

    version='0.1.1',

    description='Helper Python',
    classifiers=[
        'Development Status :: 5 - Alpha'
    ],
    keywords='helper, type checking, retry',
    package_dir={'': 'helper_python'},
    packages=find_packages(exclude=["tests"])
)
