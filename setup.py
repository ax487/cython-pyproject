from setuptools import setup, find_packages
from setuptools.extension import Extension

extensions = [
    Extension("pakname.extension",
              ['src/extension.pyx'],
              )]

setup(name="pakname",
      ext_modules=extensions,
      packages=find_packages(exclude=["tests"]),
      test_suite='tests')
