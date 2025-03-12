# python-cpp-extension

## Goal

To create a simple example how to extend Python with C++ extensions.

## Requirements

- `python3-dev` or `python3-devel` python development package
- `C++` compiler

## Build and install

`pip3 install src/` will build and install `C++` extension.

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

- `src/cpp_impl/` - C++ implementation and header file with declaration of `SieveOfEratosthenes` function
- `src/setup.py` - `setuptools` file to easily build and install the extension
- `src/cython_wrapper/` - Cython wrapper
- `src/cpython_wrapper.cpp` / CPython wrapper

`tests/test_benchmark.py` - simple file to benchmark the extension

## Credits

[ExtendingPythonTalk](https://github.com/litleleprikon/ExtendingPythonTalk) project
