cdef extern from "c_functions.h":
    int add_numbers(int a, int b)

cdef class Interop:
    cdef int a
    cdef int b

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return add_numbers(self.a, self.b)