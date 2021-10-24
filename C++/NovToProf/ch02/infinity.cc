// Operations involving 0 and infinity.

#include <iostream>
#include <limits>

constexpr double INF { std::numeric_limits<double>::infinity() };
constexpr double VALUES[] {0.0, 1.0, INF, -INF};
constexpr std::size_t NVALUES = sizeof(VALUES)/sizeof(VALUES[0]);

static void domath(double v1, double v2) {
  std::cout << v1 << " + " << v2 << " = " << (v1 + v2) << "    "
            << v1 << " - " << v2 << " = " << (v1 - v2) << "    "
            << v1 << " * " << v2 << " = " << (v1 * v2) << "    "
            << v1 << " / " << v2 << " = " << (v1 / v2) << std::endl;
}

int main(int argc, char *argv[]) {
  for (std::size_t iv = 0; iv < NVALUES; ++iv) {
    for (std::size_t jv = 0; jv < NVALUES; ++jv) {
      double v1 { VALUES[iv] };
      double v2 { VALUES[jv] };
      domath(v1, v2);
    }
  }

  return 0;
}
