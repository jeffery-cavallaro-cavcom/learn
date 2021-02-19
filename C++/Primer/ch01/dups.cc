// Reads a sequence of values and determines the number of each set of
// consecutive values.

#include <cstdlib>
#include <iostream>

int main(int argc, char *argv[]) {
  int current = 0;
  int count = 0;
  int value = 0;
  bool done = false;

  while (! done) {
    // Get the next value.
    if ( ! (std::cin >> value) ) {
      done = true;
    }

    // If this is the first value then make it current.
    if ((! done) && (count < 1)) {
      current = value;
      count = 1;
      continue;
    }

    // Report a value change.  Remember to always report the last value.
    bool differ = (! done) && (value != current);
    if (differ || (done && (count > 0))) {
      std::cout << current << " occurs " << count << " time";
      if (count > 1) std::cout << "s";
      std::cout << std::endl;
    }

    // Install a new value or count a recurring value.
    if (differ) {
      current = value;
      count = 1;
    } else {
      ++count;
    }
  }

  return EXIT_SUCCESS;
}
