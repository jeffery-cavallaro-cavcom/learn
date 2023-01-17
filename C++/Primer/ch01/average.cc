/**
 * Prompts for integers from stdin, adds them, and then computes their average.
*/

#include <iostream>

int main(int argc, char *argv[]) {
    int sum = 0;
    int count = 0;

    std::cout << "Enter some integers (^D when done): ";

    int value = 0;
    while (std::cin >> value) {
        sum += value;
        ++count;
    }

    double average = (count > 0 ? static_cast<double>(sum)/count : 0.0);
    std::cout << "\nsum = " << sum << "  average = " << average << std::endl;

    return 0;
}
