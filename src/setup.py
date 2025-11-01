import pathlib
import sysconfig

from Cython.Build import cythonize
from setuptools import Extension, setup

THIS_DIR = pathlib.Path(__file__).parent

language = "c++"
std = "c++17"

# Handle case where CFLAGS might be None
if args := sysconfig.get_config_var("CFLAGS"):
    default_compile_args = args.split()
else:
    default_compile_args = []

extra_compile_args = [f"-std={std}", "-Wall", "-Wextra", "-Werror", "-DNDEBUG", "-O3"]

print(f"Default compile arguments: {default_compile_args}")
print(f"Extra compile arguments: {extra_compile_args}")

cpython_extension = Extension(
    "cpython_sieve",
    sources=[
        str(THIS_DIR / "cpython_wrapper.cpp"),
        str(THIS_DIR / "cpp_impl/sieve.cpp"),
    ],
    extra_compile_args=extra_compile_args,
    language=language,
    include_dirs=[str(THIS_DIR / "cpp_impl")],
)

cython_extension = Extension(
    "cython_sieve",
    sources=[
        str(THIS_DIR / "cython_wrapper/wrapper.pyx"),
        str(THIS_DIR / "cpp_impl/sieve.cpp"),
    ],
    extra_compile_args=extra_compile_args,
    language=language,
    include_dirs=[str(THIS_DIR / "cpp_impl")],
)

_ = setup(
    name="cpp_python_extension",
    version="1.0.0",
    description="Example module written in C++ with Python bindings",
    ext_modules=cythonize([cython_extension]) + [cpython_extension],
    zip_safe=False,
)
