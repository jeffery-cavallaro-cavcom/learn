// Euclid's Algorithm

#include <iostream>

int main(int argc, char *argv[]) {
    int i1 {0};
    int i2 {0};

    std::cout << "Enter two non-zero integers: ";
    std::cin >> i1 >> i2;
    if ((i1 == 0) || (i2 == 0)) {
        std::cerr << "Both integers must be non-zero!" << std::endl;
        return 1;
    }

    // The C++ mod operator enforces the relationship:
    //
    //    x = y*(x/y)+(x%y)
    //
    // where '/' is an integer divide and thus the mod result can be positive
    // or negative.  For example: -50 % 3 = -2 because -50 = -16*3 + (-2).
    // Note that this differs from the mathematical definition, which requires
    // a mod to be a positive value (equivalence class).  Thus, -50 mod 3 = 1
    // because -50 = -17*3 + 1.
    //
    // We avoid these problems by converting all negative integers to positive
    // values, since that does not change the resulting GCD.
    int m = i1 < 0 ? -i1 : i1;
    int n = i2 < 0 ? -i2 : i2;

    while (n != 0) {
        int d = m / n;
        int r = m % n;
        std::cout << m << "=" << d << "*" << n << "+" << r << std::endl;
        m = n;
        n = r;
    }

    std::cout << "(" << i1 << "," << i2 << ")=" << m << std::endl;

    return 0;
}
