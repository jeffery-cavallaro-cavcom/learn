#include <cmath>
#include <iomanip>

#include "sales_item.h"

SalesItem::SalesItem(const std::string &isbn, int quantity, double price)
    : _isbn(isbn), _quantity(quantity), _revenue(quantity*price) {}

SalesItem::SalesItem(void) : SalesItem(std::string(), 0, 0.00) {}

SalesItem::SalesItem(const SalesItem &from)
    : _isbn(from._isbn), _quantity(from._quantity), _revenue(from._revenue) {}

SalesItem &SalesItem::operator=(const SalesItem &from) {
    this->_isbn = from._isbn;
    this->_quantity = from._quantity;
    this->_revenue = from._revenue;
    return *this;
}

double SalesItem::average(void) const {
    return (_quantity != 0) ? _revenue/_quantity : 0.00;
}

SalesItem &SalesItem::operator+=(const SalesItem &from) {
    this->_quantity += from._quantity;
    this->_revenue += from._revenue;
    return *this;
}

std::ostream &operator<<(std::ostream &out, const SalesItem &book) {
    out << book.isbn() << " "
        << book.quantity() << " "
        << std::setprecision(2) << std::fixed << book.revenue() << " "
        << std::setprecision(2) << std::fixed << book.average();
    return out;
}

std::istream &operator>>(std::istream &in, SalesItem &book) {
    std::string isbn;
    int quantity = 0;
    double price = 0.00;

    in >> isbn >> quantity >> price;
    book = SalesItem(isbn, quantity, price);

    return in;
}
