/**
 * Reads a sequence of integers from stdin and then reports how many times each
 * value repeats.  The count for each encountered value is maintained in a map
 * that is indexed by integer value.
*/

#include <iostream>
#include <map>

int main(int argc, char *argv[]) {
    using MapType = std::map<int, int>;

    MapType values;
    int value = 0;

    std::cout << "Enter some integers (^D when done): ";
    while (std::cin >> value) {
        ++values[value];
    }

    std::cout << std::endl;

    if (values.size() > 0) {
        for (const auto &value : values) {
            std::cout << value.first << " repeats "
                << value.second << " time(s)"
                << std::endl;
        }
    } else {
        std::cout << "No values entered" << std::endl;
    }

    std::cout << std::endl;

    return 0;
}
