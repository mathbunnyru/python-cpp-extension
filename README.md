# python-cpp-extension

## Goal

To create a simple example how to extend Python with C++ extensions.

## Requirements

- `python3-dev` or `python3-devel` python development package
- `C++` compiler

## Build and install

`python3 src/setup.py build` will build the `C++` extension.

`python3 src/setup.py install` will build and install it.

You can use `--user` flag to install to the Python user install directory.

## How to use

First, install the extension. Then you can use it like this:

```python
import cpp_python_extension

print(cpp_python_extension.sieve_of_eratosthenes(11))
```

This will print all the prime numbers from 1 to 11 (inclusive).

## Benchmarking

`python3 -m pytest tests/test_benchmark.py --verbose`

## Files

`src/`:

- `setup.py` - `setuptools` file to easily build and install the extension
- `sieve.h` - header file with declaration of `SieveOfEratosthenes` function
- `sieve.cpp` - implementation file
- `sieve_python_wrapper.cpp` - wrapper around `SieveOfEratosthenes` function to create `cpp_python_extension` module

`tests/`:

- `test_benchmark.py` - simple file to benchmark the extension

## Credits

[ExtendingPythonTalk](https://github.com/litleleprikon/ExtendingPythonTalk) project
