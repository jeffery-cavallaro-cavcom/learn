// Calculate BMI from height (feet/includes) and weight (lbs).

#include <iomanip>
#include <iostream>

constexpr double LBS_PER_KG = 2.2;
constexpr double M_PER_FT = 0.3048;
constexpr double IN_PER_FT = 12.0;

int main(int argc, char *argv[]) {
  uint feet {};
  uint inches {};
  std::cout << "Enter height in feet and inches: ";
  std::cin >> feet >> inches;

  uint lbs {};
  std::cout << "Enter weight in pounds: ";
  std::cin >> lbs;

  double w { lbs/LBS_PER_KG };
  double h { (feet + inches/IN_PER_FT)*M_PER_FT };
  double bmi = w/(h*h);

  std::cout << "BMI=" << std::fixed << std::setprecision(1)
            << bmi << std::endl;

  return 0;
}
