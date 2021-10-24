// Convert yards to yards/feet/inches.

#include <iostream>

constexpr int FEET_PER_YARD = 3;
constexpr int INCHES_PER_FOOT = 12;

int main(int argc, char *argv[]) {
  double total {};
  std::cout << "Enter yards: ";
  std::cin >> total;

  int yards { static_cast<int>(total) };
  int feet { static_cast<int>((total - yards)*FEET_PER_YARD) };
  int inches { static_cast<int>(total * FEET_PER_YARD * INCHES_PER_FOOT) %
    INCHES_PER_FOOT };

  std::cout << total << " yards = "
            << yards << " yards "
            << feet << " feet "
            << inches << " inches "
            << std::endl;

  return 0;
}
