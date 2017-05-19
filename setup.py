from setuptools import setup

setup(
    name='fooda_tweeter',
    version='0.1',
    py_modules=['fooda_tweeter'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        fooda_tweeter=fooda_tweeter:tweeter
    ''',
)