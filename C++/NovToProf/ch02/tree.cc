// Height of a tree calculated from distance and angle.

#include <cmath>
#include <iostream>

constexpr double PI = M_PI;
constexpr double RADS_PER_DEG = PI/180.0;

int main(int argc, char *argv[]) {
  double d {};
  std::cout << "How far are you from the tree? ";
  std::cin >> d;

  double h {};
  std::cout << "What is the distance from the ground to your eye?: ";
  std::cin >> h;

  double a {};
  std::cout << "What is the angle (degrees) from your eye to the top?: ";
  std::cin >> a;

  double ht { h + d*std::tan(a*RADS_PER_DEG) };
  std::cout << "The tree height is " << ht << std::endl;

  return 0;
}
