// Sums a sequence of integers and calculates their average.

#include <cstdlib>

#include <iostream>

int main(int argc, char *argv[]) {
  int sum = 0;
  int count = 0;

  std::cout << "Enter values to sum: ";
  std::cout.flush();

  int value;
  while (std::cin >> value) {
    sum += value;
    ++count;
  }

  double average = (count > 0) ? (static_cast<double>(sum) / count) : 0.0;

  std::cout << "\nSum: " << sum << "  Average: " << average << std::endl;
  return EXIT_SUCCESS;
}
