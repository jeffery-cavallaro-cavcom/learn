// Prompts for two integers, adds them, and displays the sum.

#include "input.h"

#include <cstdlib>
#include <iostream>
#include <stdexcept>

int main(int argc, char *argv[]) {
    int value1 = 0;
    int value2 = 0;
    try {
        value1 = input_integer("Enter first addend: ");
        value2 = input_integer("Enter second addend: ");
    }
    catch (const std::runtime_error &sre) {
        std::cout << sre.what() << std::endl;
        return EXIT_FAILURE;
    }
    int sum = value1 + value2;
    std::cout << "Sum: " << sum << std::endl;
    return EXIT_SUCCESS;
}
