// Default Type Conversions

#include <iostream>

int main(int argc, char *argv[]) {
    // non-zero to bool: true, zero to bool: false
    bool bvalue = 42;
    std::cout << "bool=" << std::boolalpha << bvalue << std::endl;

    return 0;
}
