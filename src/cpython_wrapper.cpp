#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "cpp_impl/sieve.h"

static_assert(PY_MAJOR_VERSION == 3, "Python 3 is expected");

#include <vector>

namespace {

PyObject* SieveOfEratosthenesWrapper(PyObject* /*self*/, PyObject* args) {
    int n;
    if (!PyArg_ParseTuple(args, "I", &n)) {
        return nullptr;
    }
    if (n < 0) {
        PyErr_SetString(PyExc_TypeError, "expected non-negative number");
        return nullptr;
    }

    std::vector<size_t> primes = abc::SieveOfEratosthenes(n);
    PyObject* result = PyList_New(primes.size());
    for (size_t i = 0; i < primes.size(); i++) {
        PyList_SetItem(result, i, PyLong_FromLong(primes[i]));
    }
    return result;
}

PyMethodDef Methods[] = {
    PyMethodDef{
        "sieve_of_eratosthenes",
        SieveOfEratosthenesWrapper,
        METH_VARARGS,
        "Return list of prime numbers until given number."
    },
    PyMethodDef{nullptr, nullptr, 0, nullptr}  /* Sentinel */
};

PyModuleDef kModuleDefinition{
    PyModuleDef_HEAD_INIT,
    "cpython_sieve",                       /* name of module */
    "Python sieve module written in C++",  /* module documentation, may be NULL */
    -1,                                    /* size of per-interpreter state of the module,
                                           or -1 if the module keeps state in global variables. */
    Methods,
    nullptr,
    nullptr,
    nullptr,
    nullptr
};

}  // namespace

extern "C" PyObject* PyInit_cpython_sieve() {
    return PyModule_Create(&kModuleDefinition);
}
