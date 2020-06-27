#include "sieve.h"

namespace abc {

std::vector<size_t> SieveOfEratosthenes(size_t n) {
    std::vector<bool> sieve(n + 1, true);
    sieve[0] = sieve[1] = false;
    std::vector<size_t> result;
    for (size_t p = 2; p <= n; p++) {
        if (sieve[p]) {
            result.push_back(p);
            for (size_t i = 2 * p; i <= n; i += p) {
                sieve[i] = false;
            }
        }
    }
    return result;
}

}  // namespace abc
