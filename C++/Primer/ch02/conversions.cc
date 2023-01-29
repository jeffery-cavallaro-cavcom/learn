/**
 * Demostrates implicit conversions.
*/

#include <iostream>

int main(int argc, char *argv[]) {
    bool b = 42;  // true (non-zero->true, zero->false)
    std::cout << "b=" << std::boolalpha << b << std::endl;

    int i = b;  // 1 (true -> 1, false -> 0)
    std::cout << "i=" << i << std::endl;

    i = 3.14;  // 3 (truncated)
    std::cout << "i=" << i << std::endl;

    double pi = i;  // 3.0
    std::cout << "pi=" << pi << std::endl;

    unsigned char c1 = -1;  // 255 (modulo-256)
    std::cout << "c1=" << static_cast<unsigned>(c1) << std::endl;

    signed char c2 = 256;  // undefined
    std::cout << "c2=" << static_cast<int>(c2) << std::endl;

    unsigned int u1 = 10, u2 = 42;
    std::cout << u2 - u1 << std::endl;  // 32
    std::cout << u1 - u2 << std::endl;  // 4294967264

    int i1 = 10, i2 = 42;
    std::cout << i2 - i1 << std::endl;  // 32
    std::cout << i1 - i2 << std::endl;  // -32

    std::cout << i1 - u1 << std::endl;  // 0
    std::cout << u1 - i1 << std::endl;  // 0

    return 0;
}
