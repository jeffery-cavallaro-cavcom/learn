#include <iostream>

int value = 1;

int main(int argc, char *argv[]) {
    std::cout << value << std::endl;  // 1
    int value = 2;
    {
        std::cout << value << std::endl;  // 2
        int value = 3;
        std::cout << value << std::endl;  // 3
    }
    std::cout << ::value << std::endl;  // 1

    return 0;
}
