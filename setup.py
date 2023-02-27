from setuptools import setup


setup(
    author='Antoine Mathurin',
    name='xnt',
    packages=['xnt', 'xnt.article'],
    include_package_data=True,
    install_requires=['flask']
)