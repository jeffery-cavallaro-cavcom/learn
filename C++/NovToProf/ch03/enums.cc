// Demonstration of new style enums.

#include <iostream>

enum class Day {
  Sunday = 1,
  Monday,
  Tuesday,
  Wednesday,
  Thursday,
  Friday,
  Saturday
};

constexpr int DAYS_IN_WEEK {7};

static Day tomorrow(Day today) {
  int itoday = static_cast<int>(today);
  int itomorrow = (itoday % DAYS_IN_WEEK) + 1;
  return static_cast<Day>(itomorrow);
}

enum class Punctuation : char {
  Exclamation = '!',
  Comma = ',',
  DoubleQuotes = '"',
  SingleQuote = '\'',
  Tilde = '~',
};

std::ostream &operator<<(std::ostream &out, Punctuation c) {
  out << static_cast<char>(c);
  return out;
}

int main(int argc, char *argv[]) {
  Day day = Day::Sunday;
  do {
    std::cout << static_cast<int>(day) << std::endl;
    day = tomorrow(day);
  } while (day != Day::Sunday);

  std::cout << Punctuation::Exclamation << " "
            << Punctuation::Comma << " "
            << Punctuation::DoubleQuotes << " "
            << Punctuation::SingleQuote << " "
            << Punctuation::Tilde
            << std::endl;

  return 0;
}
