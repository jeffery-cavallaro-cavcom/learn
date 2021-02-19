#include "input.h"

#include <sstream>
#include <stdexcept>

int string_integer(const std::string &in) {
    std::istringstream sin(in);
    return input_integer(sin);
}

int input_integer(std::istream &in) {
    int value = 0;
    in >> value;
    if (!in) {
        throw std::runtime_error("Invalid input value");
    }
    return value;
}

int prompt_integer(const std::string &prompt) {
    std::cout << prompt;
    std::cout.flush();
    return input_integer(std::cin);
}
