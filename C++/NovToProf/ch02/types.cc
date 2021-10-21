// Basic Types

#include <iostream>
#include <string>

int main(int argc, char *argv[]) {
    // Current practice is to use uniform initialization (curly braces) to
    // guard against narrowing conversions.
    int answer {42};
    std::cout << "answer=" << answer << std::endl;

    // Uniform initialization support default (0) initialization.
    bool bvalue {};
    int ivalue {};
    double dvalue {};
    std::string svalue {};
    std::cout << "bvalue=" << std::boolalpha << bvalue
              << " ivalue=" << ivalue
              << " dvalue=" << dvalue
              << " svalue=\"" << svalue << "\""
              << std::endl;

    // A single quote can be used as a digit separator (C++14).
    int million = 1'000'000'000;
    std::cout << "million=" << million << std::endl;

    // Binary literals are not possible (C++14).
    int hundred = 0b0110'0100;
    std::cout << "hundred=" << hundred << std::endl;

    int x = -50 % 3;
    std::cout << x << std::endl;

    return 0;
}
