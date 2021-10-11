#include <iostream>

int SI = 55;

int main(int argc, char *argv[]) {
  // References to Const:
  int i = 42;
  int &ri = i;
  const int &cri = i;
  std::cout << "i=" << i << " ri=" << ri << " cri=" << cri << std::endl;

  ri = 100;
  std::cout << "i=" << i << " ri=" << ri << " cri=" << cri << std::endl;

  const int &rti = 3.14;
  std::cout << "rti=" << rti << std::endl;

  // Pointers to Const:
  int *pi = &i;
  const int *cpi = &i;
  std::cout << "i=" << i << " *pi=" << *pi << " *cpi=" << *cpi << std::endl;

  *pi = -1;
  std::cout << "i=" << i << " *pi=" << *pi << " *cpi=" << *cpi << std::endl;

  // Constant Pointer:
  int *const cp = &i;
  const int *const ccp = &i;
  std::cout << "*cp=" << *cp << " *ccp" << *ccp << std::endl;

  constexpr int cei = 100;
  constexpr const int *pcei = &SI;
  std::cout << "cei=" << cei
            << " pcei=" << pcei
            << " SI=" << SI
            << " *pcei=" << *pcei
            << std::endl;

  return 0;
}
