import pytest
import cpp_python_extension


@pytest.mark.parametrize("input", [1000, 100000, 1000000])
def test_cpp(benchmark, input):
    benchmark(cpp_python_extension.sieve_of_eratosthenes, input)
