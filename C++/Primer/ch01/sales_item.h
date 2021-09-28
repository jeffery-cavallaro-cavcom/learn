#ifndef PRIMER_CH01_SALES_ITEM_H__
#define PRIMER_CH01_SALES_ITEM_H__

// Record sales of a single book in a bookstore.

#include <iostream>
#include <string>

class SalesItem {
 public:
    SalesItem(void);
    SalesItem(const std::string &isbn, int quantity, double price);
    SalesItem(const SalesItem &from);

    SalesItem &operator=(const SalesItem &from);

    const std::string &isbn(void) const {
        return _isbn;
    }

    int quantity(void) const {
        return _quantity;
    }

    double revenue(void) const {
        return _revenue;
    }

    double average(void) const;

    SalesItem &operator+=(const SalesItem &from);

 private:
    std::string _isbn;
    int _quantity;
    double _revenue;
};

std::ostream &operator<<(std::ostream &out, const SalesItem &book);
std::istream &operator>>(std::istream &in, SalesItem &book);

#endif  // PRIMER_CH01_SALES_ITEM_H__
