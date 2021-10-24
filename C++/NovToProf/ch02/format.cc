// Output Formatting Examples

#include <cmath>
#include <iomanip>
#include <iostream>

constexpr double PI = M_PI;
constexpr int IVALUE = 100;

int main(int argc, char *argv[]) {
  std::cout << "default: " << PI << std::endl;
  std::cout << "fixed: " << std::fixed << PI << std::endl;
  std::cout << "scientific: " << std::scientific << PI << std::endl;
  std::cout << "default(3): " << std::defaultfloat << std::setprecision(3)
            << PI << std::endl;
  std::cout << "fixed(3): " << std::fixed << PI << std::endl;
  std::cout << "scientific(3): " << std::scientific << PI << std::endl;

  std::cout << "octal: " << std::oct << IVALUE << std::endl;
  std::cout << "hex: " << std::hex << IVALUE << std::endl;
  std::cout << "decimal: " << std::dec << IVALUE << std::endl;

  std::cout << "octal: " << std::showbase << std::oct << IVALUE << std::endl;
  std::cout << "hex: " << std::hex << IVALUE << std::endl;
  std::cout << "decimal: " << std::dec << IVALUE << std::endl;

  std::cout << std::setw(8) << -IVALUE << std::endl;
  std::cout << std::setw(8) << std::left << -IVALUE << std::endl;
  std::cout << std::setw(8) << std::right << -IVALUE << std::endl;
  std::cout << std::setw(8) << std::internal << -IVALUE << std::endl;

  std::cout << std::setfill('*') << std::right << std::setw(8)
            << -IVALUE << std::endl;
  std::cout << std::setw(8) << std::left << -IVALUE << std::endl;
  std::cout << std::setw(8) << std::internal << -IVALUE << std::endl;

  return 0;
}
