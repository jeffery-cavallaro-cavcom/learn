/**
 * Sales item method definitions.
*/

#include <cmath>

#include "sales_item.h"

SalesItem &SalesItem::operator=(const SalesItem &from) {
    isbn_ = from.isbn_;
    quantity_ = from.quantity_;
    revenue_ = from.revenue_;

    return *this;
}

SalesItem &SalesItem::operator+=(const SalesItem &from) {
    isbn_ = from.isbn_;
    quantity_ += from.quantity_;
    revenue_ += from.revenue_;

    return *this;
}

double SalesItem::average(void) const {
    return (quantity_ > 0) ? (revenue_/quantity_) : 0.0;
}

double SalesItem::money(double amount) {
    return std::round(100.0*amount) / 100.0;
}

std::ostream &operator<<(std::ostream &out, const SalesItem &item) {
    out << item.isbn() << " "
        << item.quantity() << " "
        << SalesItem::money(item.revenue()) << " "
        << SalesItem::money(item.average());

    return out;
}

std::istream &operator>>(std::istream &in, SalesItem &item) {
    std::string isbn;
    unsigned quantity = 0;
    double price = 0.0;

    in >> isbn >> quantity >> price;
    item = SalesItem(isbn, quantity, price);

    return in;
}
