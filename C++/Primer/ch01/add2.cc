/**
 * A program to add two integers entered on stdin.
**/

#include <iostream>

int main(int argc, char *argv[]) {
    std::cout << "Enter two integers: ";
    int v1 = 0, v2 = 0;
    std::cin >> v1 >> v2;
    std::cout << v1 << " + " << v2 << " = " << (v1 + v2) << std::endl;
    return 0;
}
