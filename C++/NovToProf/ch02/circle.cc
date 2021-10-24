// Compute the diameter, circumference, and area of a circle.

#include <cmath>
#include <iomanip>
#include <iostream>

constexpr double PI = M_PI;

int main(int argc, char *argv[]) {
  double radius {};
  int precision {};
  std::cout << "Enter radius and precision: ";
  std::cin >> radius >> precision;

  double diameter { 2*radius };
  double perimeter { diameter*PI };
  double area = { PI*radius*radius };

  std::cout << std::setprecision(precision)
            << "radius=" << radius
            << " diameter=" << diameter
            << " perimeter=" << perimeter
            << " area=" << area
            << std::endl;

  return 0;
}
