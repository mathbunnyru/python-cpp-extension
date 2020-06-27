# python-cpp-extension

## Goal

To create a simple example how to extend Python with C++ extensions.

## Requirements

- `python3-dev` or `python3-devel` `Python 3` development package
- `C++` compiler

## Build and install

`python3 setup.py build` will build the `C++` extension.
`python3 setup.py install` will install it.

## Benchmarking

`pytest test_benchmark.py --verbose`

## Files

- `setup.py` - `setuptools` file to easily build and install the extension
- `sieve.h` - header file with declaration of `SieveOfEratosthenes` function
- `sieve.cpp` - implementation file
- `sieve_python_wrapper.cpp` - wrapper around `SieveOfEratosthenes` function to create `cpp_python_extension` module
- `test_benchmark.py` - simple file to benchmark the extension
