import ctypes

"""loading the C dll into loaded_dll"""
loaded_dll = ctypes.cdll.LoadLibrary(r"C:\Users\tamir\Documents\pythonProject\module6_interop\dll\libTest.dll")

print("execute SampleAddInt")
res = loaded_dll.SampleAddInt(4, 5)
print("int result ",res)
print("execute printString")

loaded_dll.printString("abcdefg")

result = loaded_dll.doubleFunc(1.2, 6.7)
#
# print(result)


