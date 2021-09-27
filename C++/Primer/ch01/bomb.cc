// Perform a countdown using a for loop.

#include <iostream>
#include <thread>

int main(int argc, char *argv[]) {
    for (int i = 10; i > 0; --i) {
        std::cout << i << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    std::cout << "BOOM!" << std::endl;
    return 0;
}
