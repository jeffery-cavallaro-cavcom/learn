// Reads the sales records for a bookstore and outputs a sales report.

#include <cstdlib>
#include <iostream>

#include "sales_item.h"

int main(int argc, char *argv[]) {
  // Process records until EOF or error.
  SalesItem book;
  while (std::cin >> book) {
    std::cout << book;
  }

  return EXIT_SUCCESS;
}

