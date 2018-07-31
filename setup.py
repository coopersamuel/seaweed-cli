'''
    This setup file tells python how to run the cli
'''

from setuptools import setup

setup(
    name = 'seaweed',
    version = '0.1.0',
    packages = ['seaweed'],
    entry_points = {
        'console_scripts': [
            'seaweed = seaweed.__main__:main'
        ]
    }
)