#include "input.h"

#include <iostream>

int input_integer(const std::string &prompt) {
    std::cout << prompt;
    std::cout.flush();
    int value = 0;
    std::cin >> value;
    return value;
}
