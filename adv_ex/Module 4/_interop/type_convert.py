import ctypes

"""loading the C dll into loaded_dll"""
loaded_dll = ctypes.cdll.LoadLibrary(r"C:\Users\tamir\Documents\pythonProject\module6_interop\dll\libTest.dll")

val1, val2 = ctypes.c_double(11.3), ctypes.c_double(12.4)

res = loaded_dll.doubleFunc(val1, val2)
print("doubleFunc result-", res)

"""need to convert the result !!!!"""
loaded_dll.doubleFunc.restype = ctypes.c_double
res = loaded_dll.doubleFunc(val1, val2)
print("doubleFunc result After-", res)

"""The b prefix signifies a bytes string literal."""
loaded_dll.printString(b"my text from bytes")

"""defining an argument type"""

# declare the functions we use
loaded_dll.strFunction.argtypes = [ctypes.c_char_p]
loaded_dll.strFunction.restype = ctypes.c_char_p

str_result = loaded_dll.strFunction("Tamir".encode())
print("str_result-", str_result)


class PointClass(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)
    ]

loaded_dll.structFunc.restype = ctypes.POINTER(PointClass)
my_point = PointClass(100,200)
res =  loaded_dll.structFunc(my_point)
print("my point = ",res)
print (res.contents.x, res.contents.y)

