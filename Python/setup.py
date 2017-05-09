from codecs import open
from setuptools import setup, find_packages


try:
    long_description = open('README.md').read()
except IOError:
    long_description = ''

setup(
    name='ray-tracer',
    version='0.1.0',
    author='',
    author_email='',
    packages=find_packages(),
    url='https://github.com/rozdemir/RayTrace/',
    description='',
    long_description=long_description,
    install_requires=[],
    include_package_data=True,
    keywords='Ray Tracer',
    zip_safe=False,
    license='',
    platforms=['any'],
)



