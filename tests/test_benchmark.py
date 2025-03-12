# type: ignore
import cpython_sieve
import cython_sieve
import pytest


@pytest.mark.parametrize("input", [1000, 100000, 1000000])
def test_cpython(benchmark, input):
    benchmark(cpython_sieve.sieve_of_eratosthenes, input)


@pytest.mark.parametrize("input", [1000, 100000, 1000000])
def test_cython(benchmark, input):
    benchmark(cython_sieve.sieve_of_eratosthenes, input)
