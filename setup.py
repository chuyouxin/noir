from setuptools import setup

setup(
    name='nori',
    version='0.0.1',
    description='fast web framework',
    author='ryou zhang',
    author_email='ryouzhang@gmail.com',
    install_requires=['uvloop', 'aiohttp', 'toml'],
    py_modules=['nori'],
    licence='Licence :: MTI Lecence'
)