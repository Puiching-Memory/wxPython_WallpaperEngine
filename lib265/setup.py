from setuptools import setup,Extension,find_packages
from Cython.Build import cythonize
import os

package_dir = {
    'pylibde265': './lib',
}

ext_modules = [
    Extension("pylibde265",
              sources=["pylibde265.pyx"],
              include_dirs=[os.path.abspath('./lib/')],
              libraries=['de265'],
              #language='c++',
              #extra_compile_args=['-std=c++11'],
              )
]

setup(
    name='pylibde265',
    ext_modules=cythonize(ext_modules),
)