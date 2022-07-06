import sysconfig

from Cython.Build import cythonize
from setuptools import Extension, setup

language = "c++"
std = "c++17"

default_compile_args = sysconfig.get_config_var("CFLAGS").split()
extra_compile_args = [f"-std={std}", "-Wall", "-Wextra", "-Werror", "-DNDEBUG", "-O3"]

print(f"Default compile arguments: {default_compile_args}")
print(f"Extra compile arguments: {extra_compile_args}")

extension = Extension(
    "cpp_python_extension",
    sources=["sieve_python_wrapper.cpp", "sieve.cpp"],
    extra_compile_args=extra_compile_args,
    language=language,
)

cython_extension = Extension(
    "cython_sieve",
    sources=["cython_sieve.pyx", "sieve.cpp"],
    extra_compile_args=extra_compile_args,
    language="c++",
)

setup(
    name="cpp_python_extension",
    version="1.0",
    description="This is Example module written in C++",
    ext_modules=cythonize([extension, cython_extension]),
)
