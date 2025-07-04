from setuptools import setup, find_packages

setup(
    name='python_web_filter',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'scapy',
        'PyYAML',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'web-filter=main:main'
        ]
    },
)
