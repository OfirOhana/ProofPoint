from setuptools import setup, find_packages


def get_version():
    import os

    version_path = os.path.join(os.path.abspath(os.path.curdir), 'weather', 'version.txt')
    with open(version_path, 'r') as f:
        return f.read()


setup(
    name='weather',
    version=get_version(),
    description='Get the weather status of the given city.',
    packages=find_packages(),
    install_requires=[
        'requests'
    ]
)
