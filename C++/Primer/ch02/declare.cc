// The variable is declared for use here, but is defined elsewhere.

extern int GLOBAL;
extern const int CONST_GLOBAL;
const int LOCAL = 123;

#include <iostream>

int main(int argc, char *argv[]) {
    std::cout << "GLOBAL=" << GLOBAL << std::endl;
    std::cout << "CONST_GLOBAL=" << CONST_GLOBAL << std::endl;
    std::cout << "LOCAL=" << LOCAL << std::endl;
    return 0;
}
