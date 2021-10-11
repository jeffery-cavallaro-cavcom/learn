#include <iostream>

int main(int argc, char *argv[]) {
  // Type Alias (formally typedef):
  using pint = int *;

  int i = 42;
  const pint pi = &i;  // pi is const
  std::cout << "pi=" << pi << " *pi=" << *pi << std::endl;

  *pi = 100;
  std::cout << "pi=" << pi << " *pi=" << *pi << std::endl;

  // Auto:
  auto ai = 10;  // int ai
  auto *pai = &ai;  // int *pai
  auto &rai = ai;  // int &rai
  const auto cai = 42;  // const int cai
  auto xai = cai;  // int xai, ignores top-level const
  const auto &cxai = cai;  // const int &cxai, must specify top-level const

  std::cout << "ai=" << ai
            << " *pai=" << *pai
            << " rai=" << rai
            << " cai=" << cai
            << " xai=" << xai
            << " cxai=" << cxai
            << std::endl;

  xai = 50;
  std::cout << "xai=" << xai << std::endl;

  // Decltype:
  const int cj = 10, &rcj = cj;
  decltype(cj) x = 20;  // const int x
  decltype(rcj) y = x;  // const int &y, keeps top-level const
  decltype(rcj + 0) z = -1;  // int z, type of expression
  decltype(*pai) w = i;  // int &w, due to lvalue
  decltype((i)) v = i;  // int &v, due to lvalue expression
  std::cout << "i=" << i
            << " cj=" << cj
            << " rcj=" << rcj
            << " x=" << x
            << " y=" << y
            << " z=" << z
            << " w=" << w
            << " v=" << v
            << std::endl;

  z = 2;
  w = 10;
  std::cout << "z=" << z
            << " w=" << w
            << " v=" << v
            << " i=" << i
            << std::endl;
  
  return 0;
}
