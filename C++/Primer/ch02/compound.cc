/**
 * Demonstrates compound types.
*/

#include <iostream>

int main(int argc, char *argv[]) {
    // reference:
    int i = 42;
    int &ri = i;
    std::cout << "i=" << i << " ri=" << ri << std::endl;
    ri = 100;
    std::cout << "i=" << i << " ri=" << ri << std::endl;

    // pointer:
    int *pi = &i;
    std::cout << "i=" << i << " *pi=" << *pi << std::endl;
    *pi = -1;
    std::cout << "i=" << i << " *pi=" << *pi << std::endl;

    // void pointer:
    void *vpi = &i;
    i = 60;
    std::cout << "i=" << i << " *vpi=" << *reinterpret_cast<int *>(vpi)
        << std::endl;

    // pointer to pointer:
    int **ppi = &pi;
    **ppi = 99;
    std::cout << "i=" << i << " **ppi=" << **ppi << std::endl;

    // reference to pointer:
    int *&rpi = pi;
    *pi = 123;
    std::cout << "i=" << i << " *rpi=" << *rpi << std::endl;

    return 0;
}
