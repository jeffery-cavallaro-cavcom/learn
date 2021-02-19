// Prompts for two integers, adds them, and displays the sum.

#include "input.h"

#include <cstdlib>

#include <stdexcept>

int main(int argc, char *argv[]) {
    int value1 = 0;
    int value2 = 0;
    try {
        value1 = prompt_integer("Enter first addend: ");
        value2 = prompt_integer("Enter second addend: ");
    }
    catch (const std::runtime_error &rte) {
        std::cerr << "\n" << rte.what() << std::endl;
        return EXIT_FAILURE;
    }
    int sum = value1 + value2;
    std::cout << "\nSum: " << sum << std::endl;
    return EXIT_SUCCESS;
}
