#ifndef __SALES_ITEM_H__
#define __SALES_ITEM_H__

/**
 * Sales Item
 * 
 * Each raw sales item is of the form:
 * 
 *      isbn quantity price
 * 
 * The data is stored internally as isbn, quantity, revenue.
*/

#include <iostream>
#include <string>

class SalesItem {
 public:
    SalesItem(void): quantity_(0), revenue_(0.0) {}

    SalesItem(const std::string &isbn, unsigned quantity, double price) :
        isbn_(isbn), quantity_(quantity), revenue_(quantity*price) {}

    SalesItem(const SalesItem &from) :
        isbn_(from.isbn_),
        quantity_(from.quantity_),
        revenue_(from.revenue_) {}

    SalesItem &operator=(const SalesItem &from);
    SalesItem &operator+=(const SalesItem &from);

    const std::string &isbn(void) const { return isbn_; }
    unsigned quantity(void) const { return quantity_; }
    double revenue(void) const { return revenue_; }

    double average(void) const;

    static double money(double amount);

 private:
    std::string isbn_;
    unsigned quantity_;
    double revenue_;
};

std::ostream &operator<<(std::ostream &out, const SalesItem &item);
std::istream &operator>>(std::istream &in, SalesItem &item);

#endif  // __SALES_ITEM_H__
