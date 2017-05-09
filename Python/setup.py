from codecs import open

from Cython.Build import cythonize
from setuptools import setup, find_packages
from distutils.core import setup
from distutils.extension import Extension
try:
    from Cython.Distutils import build_ext
except ImportError:
    use_cython = False
else:
    use_cython = True

cmdclass = { }
ext_modules = [ ]
extensions = [Extension("*", ["*.py"])]

if use_cython:
    ext_modules += [
        Extension("khudi", ["khudi/main.py"]),
        #Extension("khudi/color", ["khudi/color/*.py"]),
        #Extension("khudi/image", ["khudi/image/*.py"]),

    ]
    cmdclass.update({ 'build_ext': build_ext })
else:
    ext_modules += [
        Extension("khudi", [ "khudi/*.c" ]),
    ]

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ''

setup(
    name='ray-tracer',
    version='0.1.0',
    author='',
    author_email='',
    packages=[],
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
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



