/**
 * Demonstrates variable definitions, declarations, and initialization.
*/

#include <iostream>

extern double pi;  // declaration
extern double euler;  // declaration

int i0;  // Default initialized to 0.

int main(int argc, char *argv[]) {
    int i1;  // undefined
    int i2 = 2;
    int i3(3);
    int i4 = (4);
    int i5{5};  // prevents loss of information
    int i6 = {6};  // prevents loss of information

    std::cout << "i0=" << i0 << std::endl;
    std::cout << "i2=" << i2 << std::endl;
    std::cout << "i3=" << i3 << std::endl;
    std::cout << "i4=" << i4 << std::endl;
    std::cout << "i5=" << i5 << std::endl;
    std::cout << "i6=" << i6 << std::endl;

    std::cout << "pi=" << pi << std::endl;
    std::cout << "e=" << euler << std::endl;

    return 0;
}
