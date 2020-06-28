cimport sieve

def sieve_of_eratosthenes(size_t n):
    '''
    Return list of prime numbers until given number. Implemented in Cython.
    '''
    return sieve.SieveOfEratosthenes(n)
