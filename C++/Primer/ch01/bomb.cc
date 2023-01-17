/**
 * A countdown from 10 to 0 with a boom at the end.
*/

#include <iostream>
#include <thread>
#include <chrono>

int main(int argc, char *argv[]) {
    for (int i = 10; i > 0; --i) {
        std::cout << i << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    std::cout << "BOOM !!!" << std::endl;

    return 0;
}
