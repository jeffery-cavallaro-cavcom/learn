// The variable is declared for use here, but is defined elsewhere.

extern int GLOBAL;

#include <iostream>

int main(int argc, char *argv[]) {
    std::cout << "GLOBAL=" << GLOBAL << std::endl;
    return 0;
}
