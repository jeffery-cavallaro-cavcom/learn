// Demonstrates counting down with a for loop.  The starting value is specified
// on the command line and defaults to 10.

#include <cstdlib>

#include <stdexcept>

#include "input.h"

int main(int argc, char *argv[]) {
    int count = 10;
    try {
        if (argc > 1) count = string_integer(argv[1]);
    }
    catch (const std::runtime_error &rte) {
        std::cerr << "Invalid start value" << std::endl;
        return EXIT_FAILURE;
    }

    if (count < 0) count = -count;

    for (int i = count; i >= 0; --i) {
        std::cout << i << std::endl;
    }

    std::cout << "BOOM !!!" << std::endl;

    return EXIT_SUCCESS;
}
