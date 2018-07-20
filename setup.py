from setuptools import setup, find_packages

setup(
    name='helper',
    version='0.9.0',

    description='Helper Python',
    classifiers=[
        'Development Status :: 4 - Beta'
    ],
    keywords='helper, type checking, retry',
    package_dir={'': 'helper_python'},
    packages=find_packages('helper_python', exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
)
