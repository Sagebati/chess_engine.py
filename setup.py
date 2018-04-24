from distutils.core import setup
from Cython.Build import cythonize
from setuptools import Extension, find_packages

setup(
    name="Quetzal",
    packages=find_packages(),
    ext_modules=cythonize(Extension("*", ["*/*.pyx"])),
    install_requires=['python-chess', 'cython']
)
