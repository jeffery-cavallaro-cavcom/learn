#include <iostream>

int main(int argc, char *argv[]) {
    int answer = 42;
    int &life = answer;
    std::cout << "life=" << life << " answer=" << answer << std::endl;

    life = 100;
    std::cout << "life=" << life << " answer=" << answer << std::endl;

    return 0;
}
