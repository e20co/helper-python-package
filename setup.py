from setuptools import setup, find_packages

setup(
    name='helper',
    version='0.1.2',

    description='Helper Python',
    classifiers=[
        'Development Status :: 3 - Alpha'
    ],
    keywords='helper, type checking, retry',
    package_dir={'': 'helper_python'},
    packages=find_packages('helper_python')
)
