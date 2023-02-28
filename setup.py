from setuptools import setup, find_packages


setup(
    author='Antoine Mathurin',
    name='xnt',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['flask', 'opensearch-py', 'openai', 'feedparser']
)