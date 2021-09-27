// Count how many times each nonnegative number has occurred in an input
// sequence.

#include <iostream>
#include <map>

using Numbers = std::map<int, uint>;

int main(int argc, char *argv[]) {
    Numbers numbers;
    int next;

    std::cout << "Enter number sequence: ";

    while (std::cin >> next) {
        if (next >= 0) {
            Numbers::value_type entry(next, 0);
            auto inserted = numbers.insert(entry);
            ++(inserted.first->second);
        } else {
            std::cout << "Ignoring negative value " << next << std::endl;
        }
    }

    for (auto number : numbers) {
        std::cout << number.first << " occurred "
                  << number.second << " time(s)"
                  << std::endl;
    }

    return 0;
}
