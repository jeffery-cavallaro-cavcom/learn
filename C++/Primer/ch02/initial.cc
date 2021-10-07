#include <iostream>

int main(int argc, char *argv[]) {
    // Initialization Syntaxes:
    int zero = int();
    int one = 1;
    int two = {2};  // disallows loss of info
    int three{3};  // disallows loss of info
    int four(4);

    std::cout << zero << " "
              << one << " "
              << two << " "
              << three << " "
              << four << std::endl;

    return 0;
}
