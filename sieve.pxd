from libcpp.vector cimport vector


cdef extern from "sieve.h" namespace "abc":
    vector[size_t] SieveOfEratosthenes(size_t n)
