// Reads a sequence of integers and computes their sum and average.

#include <iostream>

int main(int argc, char *argv[]) {
    int sum = 0;
    int n = 0;
    int i;

    std::cout << "Enter numbers: ";

    while (std::cin >> i) {
        sum += i;
        ++n;
    }

    double average = (n > 0) ? static_cast<double>(sum)/n : 0;

    std::cout << "\nSUM = " << sum << "  AVG = " << average << std::endl;

    return 0;
}
