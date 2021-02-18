#include "input.h"

#include <sstream>
#include <stdexcept>

int string_integer(const std::string &in) {
    std::istringstream sin(in);
    return input_integer(sin);
}

int input_integer(const std::string &prompt) {
    std::cout << prompt;
    std::cout.flush();
    int value = 0;
    std::cin >> value;
    if (!std::cin.good()) {
        throw std::runtime_error("Invalid input value");
    }
    return value;
}
