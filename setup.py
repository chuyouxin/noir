from distutils.core import setup

setup(
    name='nori',
    version='0.0.1',
    description='fast web framework',
    author='ryou zhang',
    author_email='ryouzhang@gmail.com',
    install_requires=['uvloop', 'aiohttp', 'toml'],
    url='https://github.com/RyouZhang/nori/',
    packages=['nori'],
    licence='Licence :: MTI Lecence'
)