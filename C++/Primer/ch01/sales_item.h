#ifndef PRIMER_CH01_SALES_ITEM_H_
#define PRIMER_CH01_SALES_ITEM_H_

// Records the revenue and number of copies sold of a particular book in a
// bookstore.  Books are identified by ISBN.

#include <iostream>
#include <string>

class SalesItem {
 public:
  SalesItem(const std::string &isbn = std::string(),
            unsigned int quantity = 0,
            double price = 0.0);

  // Assignment:
  SalesItem &operator=(const SalesItem &from);

  // Accessors:
  const std::string &isbn(void) const { return isbn_; }
  unsigned int quantity(void) const { return quantity_; }
  double revenue(void) const { return revenue_; }

  // Returns the average cost per book sold.
  double average(void) const;

 private:
  std::string isbn_;
  unsigned int quantity_;
  double revenue_;

  // Used in copy and assignment.
  void copy_item(const SalesItem &from);

  // Returns a double value rounded to two decimal places.
  static double money_round(double value);

  friend std::istream &operator>>(std::istream &in, SalesItem &book);
};

// Reads a sales record: isbn quantity price
std::istream &operator>>(std::istream &in, SalesItem &book);

// Writes a book report: isbn quantity revenue average
std::ostream &operator<<(std::ostream &out, const SalesItem &book);

#endif  // PRIMER_CH01_SALES_ITEM_H_
