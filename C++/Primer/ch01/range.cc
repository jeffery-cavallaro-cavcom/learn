// Generates a range between two values (inclusive) with a specified step.  All
// values are obtained from the command line.  Missing endpoint values default
// to 0.  A missing step value defaults to 1.
//
// Usage:    range [start [end [step]]]
//

#include <cstdlib>

#include <stdexcept>

#include "input.h"

int main(int argc, char *argv[]) {
    int start = 0;
    int end = 0;
    int step = 1;

    try {
        if (argc > 1) start = string_integer(argv[1]);
        if (argc > 2) end = string_integer(argv[2]);
        if (argc > 3) step = string_integer(argv[3]);
    }
    catch (const std::runtime_error &rte) {
        std::cerr << rte.what() << std::endl;
        return EXIT_FAILURE;
    }

    // Make sure that the starting value is less than the ending value.
    if (start > end) {
        int tmp = start;
        start = end;
        end = tmp;
    }

    // Disallow zero steps.
    if (step == 0) {
        std::cerr << "Invalid step value" << std::endl;
        return EXIT_FAILURE;
    }

    // Make sure that the step has the appropriate sign.
    if (step < 0) step = -step;

    // Generate the range.
    int i = start;
    while (i <= end) {
        std::cout << i << std::endl;
        i += step;
    }

    return EXIT_SUCCESS;
}
