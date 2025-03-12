# type: ignore
import cpp_python_extension
import cython_sieve
import pytest


@pytest.mark.parametrize("input", [1000, 100000, 1000000])
def test_cpp(benchmark, input):
    benchmark(cpp_python_extension.sieve_of_eratosthenes, input)


@pytest.mark.parametrize("input", [1000, 100000, 1000000])
def test_cyth(benchmark, input):
    benchmark(cython_sieve.sieve_of_eratosthenes, input)
