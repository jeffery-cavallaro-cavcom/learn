#include "sales_item.h"

#include <cmath>

#include <iomanip>
#include <stdexcept>

SalesItem::SalesItem(const std::string &isbn,
                     unsigned int quantity,
                     double price) : isbn_(isbn),
                                     quantity_(quantity),
                                     revenue_(money_round(quantity*price)) {}

SalesItem::SalesItem(const SalesItem &from) {
  copy_item(from);
}

SalesItem &SalesItem::operator=(const SalesItem &from) {
  copy_item(from);
  return *this;
}

SalesItem &SalesItem::operator+=(const SalesItem &from) {
  if (this->isbn_ != from.isbn_) {
    throw std::runtime_error("ISBNs do not match");
  }
  this->quantity_ += from.quantity_;
  this->revenue_ += from.revenue_;
  return *this;
}

double SalesItem::average(void) const {
  return (quantity_ > 0) ? money_round(revenue_ / quantity_) : 0.0;
}

void SalesItem::copy_item(const SalesItem &from) {
  this->isbn_ = from.isbn_;
  this->quantity_ = from.quantity_;
  this->revenue_ = from.revenue_;
}

double SalesItem::money_round(double value) {
  return round(100*value) / 100;
}

std::istream &operator>>(std::istream &in, SalesItem &book) {
  std::string isbn;
  unsigned int quantity = 0;
  double price = 0.0;

  bool valid = (in >> isbn) && (in >> quantity) && (in >> price);
  if (!valid) {
    isbn.clear();
    quantity = 0;
    price = 0.0;
  }
  book = SalesItem(isbn, quantity, price);

  return in;
}

std::ostream &operator<<(std::ostream &out, const SalesItem &book) {
  out << book.isbn() << " "
      << book.quantity() << " "
      << std::setprecision(2) << std::fixed << book.revenue() << " "
      << std::setprecision(2) << std::fixed << book.average();
  return out;
}
