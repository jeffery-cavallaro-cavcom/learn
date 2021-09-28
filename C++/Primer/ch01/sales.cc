// Produce a bookstore sales report.

#include <iostream>
#include <map>

#include "sales_item.h"

using Books = std::map<std::string, SalesItem>;

int main(int argc, char *argv[]) {
    Books books;
    SalesItem book;

    while (std::cin >> book) {
        auto result = books.emplace(book.isbn(), book);
        if (!result.second) result.first->second += book;
    }

    for (const auto book : books) {
        std::cout << book.second << std::endl;
    }

    return 0;
}
