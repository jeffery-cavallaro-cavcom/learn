/**
 * Sales item test driver.
*/

#include <iostream>
#include <map>

#include "sales_item.h"

using MapType = std::map<std::string, SalesItem>;

int main(int argc, char *argv[]) {
    MapType sales;

    SalesItem sale;

    while (std::cin >> sale) {
        SalesItem &current = sales[sale.isbn()];
        current += sale;
    }

    for (const auto &item : sales) {
        std::cout << item.second << std::endl;
    }

    return 0;
}
