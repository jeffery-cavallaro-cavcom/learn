/**
 * Demonstrates variable scope.
*/

#include <iostream>

int answer = 42;

int main(int argc, char *argv[]) {
    std::cout << answer << std::endl;  // 42

    {
        int answer = 100;
        std::cout << answer << std::endl;  // 100

        for (int answer = 0; answer < 10; ++answer) {
            std::cout << answer << std::endl;
        }

        std::cout << answer << std::endl;  // 100
    }

    std::cout << answer << std::endl;  // 42

    return 0;
}
