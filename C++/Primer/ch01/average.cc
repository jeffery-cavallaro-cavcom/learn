/**
 * Determines the average of a sequence of integers obtained from stdin.
**/

#include <iostream>

int main(int argc, char *argv[]) {
    int sum = 0;
    int count = 0;
    std::cout << "Enter some integers (^D when done): ";
    int next = 0;
    while (std::cin >> next) {
        sum += next;
        ++count;
    }
    double average = 0.0;
    if (count > 0) {
        average = static_cast<double>(sum) / count;
    }
    std::cout << "\nCount = " << count
        << " Sum = " << sum
        << " Average = " << average
        << std::endl;
    return 0;
}
