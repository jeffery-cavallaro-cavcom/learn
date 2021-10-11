#include <iostream>

void show(int i, int &ri, int *pi, int **ppi, int *&rpi) {
  std::cout << "ni=" << i << std::endl;
  std::cout << "ri=" << ri << std::endl;
  std::cout << "pi=" << pi << std::endl;
  std::cout << "*pi=" << *pi << std::endl;
  std::cout << "ppi=" << ppi << std::endl;
  std::cout << "*ppi=" << *ppi << std::endl;
  std::cout << "**ppi=" << **ppi << std::endl;
  std::cout << "rpi=" << rpi << std::endl;
  std::cout << "*rpi=" << *rpi << std::endl;
  std::cout << std::endl;
};

int main(int argc, char *argv[]) {
  int i = 42, &ri = i, *pi = &i, **ppi = &pi, *&rpi = pi;
  show(i, ri, pi, ppi, rpi);

  ri = 1;
  show(i, ri, pi, ppi, rpi);

  *pi = 2;
  show(i, ri, pi, ppi, rpi);

  **ppi = 3;
  show(i, ri, pi, ppi, rpi);

  pi = nullptr;
  std::cout << "pi=" << pi << std::endl;
  
  return 0;
}
