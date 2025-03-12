from libcpp.vector cimport vector


cdef extern from "../cpp_impl/sieve.h" namespace "abc":
    vector[size_t] SieveOfEratosthenes(size_t n)
