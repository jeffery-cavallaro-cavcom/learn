/**
 * Prompts for two integers from stdin, adds them, and displays the results.
*/

#include <iostream>

int main(int argc, char *argv[]) {
    std::cout << "Enter two numbers: ";
    int v1 = 0, v2 = 0;
    std::cin >> v1 >> v2;
    std::cout << v1 << " + " << v2 << " = " << (v1 + v2) << std::endl;
    return 0;
}
