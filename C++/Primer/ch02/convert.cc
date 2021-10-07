// Default Type Conversions

#include <iostream>
#include <iomanip>

int main(int argc, char *argv[]) {
    // non-zero to bool: true, zero to bool: false
    bool bvalue = 42;
    std::cout << "bool=" << std::boolalpha << bvalue << std::endl;
    bvalue = 0;
    std::cout << "bool=" << std::boolalpha << bvalue << std::endl;

    // true to int: 1, false to int: 0
    int ivalue = true;
    std::cout << "int=" << ivalue << std::endl;
    ivalue = false;
    std::cout << "int=" << ivalue << std::endl;

    // double to int: truncate
    ivalue = 3.14;
    std::cout << "int=" << ivalue << std::endl;

    // int to double: extend
    double dvalue = 3;
    std::cout << "double="
              << std::fixed << std::setprecision(1) << dvalue
              << std::endl;

    // overflow unsigned: modulo number of values
    unsigned char ucvalue = -5;  // 251
    std::cout << "ucvalue=" << static_cast<int>(ucvalue) << std::endl;

    // overflow signed: undefined
    signed char scvalue = 200;
    std::cout << "scvalue=" << static_cast<int>(scvalue) << std::endl;

    // Mixing unsigned and signed converts to unsigned
    unsigned int uivalue = 10;
    int sivalue = -42;
    std::cout << "ui+si=" << uivalue + sivalue << std::endl;  // 4294967264

    return 0;
}
