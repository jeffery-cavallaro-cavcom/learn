// A simple hello world program.  Exits with an error status if any arguments
// are specified.

#include <cstdlib>

#include <iostream>

int main(int argc, char *argv[]) {
    std::cout << "Hello, World!!!" << std::endl;
    return (argc > 1) ? EXIT_FAILURE : EXIT_SUCCESS;
}
