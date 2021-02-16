// Prompts for two integers, adds them, and displays the sum.

#include "input.h"

#include <cstdlib>
#include <iostream>

int main(int argc, char *argv[]) {
    int value1 = input_integer("Enter first addend: ");
    int value2 = input_integer("Enter second addend: ");
    int sum = value1 + value2;
    std::cout << "Sum: " << sum << std::endl;
    return EXIT_SUCCESS;
}
