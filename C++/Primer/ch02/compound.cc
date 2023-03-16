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

    // reference to const:
    const int &cri = i;
    std::cout << "i=" << i << " ri=" << ri << " cri=" << cri << std::endl;
    ri = 1024;
    std::cout << "i=" << i << " ri=" << ri << " cri=" << cri << std::endl;

    // temporary use:
    double pie = 3.14;
    const int &pii = pie;
    std::cout << "pie=" << pie << " pii=" << pii << std::endl;
    pie *= 2;
    std::cout << "pie=" << pie << " pii=" << pii << std::endl;

    // pointer to const:
    const double *cpie = &pie;
    std::cout << "pie=" << pie << " *cpie=" << *cpie << std::endl;
    pie /= 2;
    std::cout << "pie=" << pie << " *cpie=" << *cpie << std::endl;

    // const pointer:
    int *const cpi = &i;
    std::cout << "i=" << i << " *cpi=" << *cpi << std::endl;
    *cpi = 100;
    std::cout << "i=" << i << " *cpi=" << *cpi << std::endl;

    // const pointer to const:
    const int *const cpci = &i;
    std::cout << "i=" << i << " *cpci=" << *cpci << std::endl;
    i = 5;
    std::cout << "i=" << i << " *cpci=" << *cpci << std::endl;

    return 0;
}
