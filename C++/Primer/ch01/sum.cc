// Sum the numbers from 1 to 10 using a while loop.

#include <iostream>

int main(int argc, char *argv[]) {
    int i = 1;
    int sum = 0;
    while (i <= 10) {
        sum += i;
        ++i;
    }
    std::cout << "SUM = " << sum << std::endl;
    return 0;
}
