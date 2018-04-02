from setuptools import setup, find_packages

setup(
    name='fe-mopi-sdk',
    version='0.1',
    description='MOPI SKD',
    url='https://github.com/fernandoe/fe-mopi-sdk',
    author='Fernando Espíndola',
    author_email='fer.esp@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'requests>=2.18.4',
    ]
)
