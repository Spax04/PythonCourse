#include <stdio.h>
#include <dlfcn.h>

typedef int (*AddFunc)(int, int);

int main() {
    void* handle = dlopen("./interop.so", RTLD_LAZY);
    if (!handle) {
        fprintf(stderr, "Error: %s\n", dlerror());
        return 1;
    }

    AddFunc add_numbers = (AddFunc)dlsym(handle, "Interop_add");
    if (!add_numbers) {
        fprintf(stderr, "Error: %s\n", dlerror());
        dlclose(handle);
        return 1;
    }

    int a = 5;
    int b = 7;
    int result = add_numbers(a, b);
    printf("Result: %d\n", result);

    dlclose(handle);
    return 0;
}