// Convert (yards feet inches) to inches and then back.

#include <iostream>

const uint FEET_PER_YARD {3};
const uint INCHES_PER_FOOT {12};

int main(int argc, char *argv[]) {
  uint yards {}, feet {}, inches {};
  std::cout << "Input yards feet inches: ";
  std::cin >> yards >> feet >> inches;

  uint total = INCHES_PER_FOOT*(feet + FEET_PER_YARD*yards) + inches;

  std::cout << yards << " yard " << feet << " feet " << inches << " inches = "
            << total << " inches"
            << std::endl;

  inches = total;

  feet = inches/INCHES_PER_FOOT;
  inches %= INCHES_PER_FOOT;

  yards = feet/FEET_PER_YARD;
  feet %= FEET_PER_YARD;

  std::cout << total << " inches = "
            << yards << " yards "
            << feet << " feet "
            << inches << " inches"
            << std::endl;

  return 0;
}
