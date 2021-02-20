// Reads the sales records for a bookstore and outputs a sales report.

#include <cstdlib>
#include <iostream>
#include <map>

#include "sales_item.h"

using BookMap = std::map<std::string, SalesItem>;

int main(int argc, char *argv[]) {
  BookMap books;

  // Process records until EOF or error.
  SalesItem book;
  while (std::cin >> book) {
    auto result = books.emplace(book.isbn(), book);
    if (!result.second) result.first->second += book;
  }

  // Output the report.
  for (const auto book : books) {
    std::cout << book.second << std::endl;
  }

  return EXIT_SUCCESS;
}

