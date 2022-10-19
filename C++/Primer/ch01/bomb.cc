/**
 * A simple countdown from 10 to 0.
**/

#include <chrono>
#include <iostream>
#include <thread>

int main(int argc, char *argv[]) {
    for (int tick = 10; tick > 0; --tick) {
        std::cout << tick << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    std::cout << "BOOM !!!" << std::endl;
    return 0;
}
