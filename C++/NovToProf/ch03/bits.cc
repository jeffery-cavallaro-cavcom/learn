// Bit Operations

#include <iomanip>
#include <iostream>
#include <string>

constexpr uint RED { 0xFF0000 };
constexpr uint WHITE { 0xFFFFFF };
constexpr uint MASK { RED^WHITE };
constexpr uint FLAGS { 0xFF };
constexpr uint BIT1 { 1 << 1 };
constexpr uint BIT6 { 1 << 6 };
constexpr uint BIT20 { 1 << 20 };

static void do_negate(const std::string &name, uint value) {
  std::cout << name << ": " << std::setw(8) << value << std::endl;
  std::cout << "~" << name << ": " << std::setw(8) << ~value << std::endl;
}

static void do_and(const std::string &name, uint v1, uint v2) {
  std::cout << name << ": " << std::setw(8) << (v1 & v2) << std::endl;
}

static void do_or(const std::string &name, uint v1, uint v2) {
  std::cout << name << ": " << std::setw(8) << (v1 | v2) << std::endl;
}

static void do_xor(const std::string &name, uint v1, uint v2) {
  std::cout << name << ": " << std::setw(8) << (v1 ^ v2) << std::endl;
}

static void get_bit(uint bits, uint pos, uint mask) {
  std::cout << "Bit " << std::dec << pos << ": "
            << std::hex << std::setw(8) << (bits & mask)
            << std::endl;
}

static void set_off(uint bits, uint pos, uint mask) {
  std::cout << "Off " << std::dec << pos << ": "
            << std::hex << std::setw(8) << (bits & ~mask)
            << std::endl;
}

static void set_on(uint bits, uint pos, uint mask) {
  std::cout << "On " << std::dec << pos << ": "
            << std::hex << std::setw(8) << (bits | mask)
            << std::endl;
}

static void set_toggle(uint bits, uint pos, uint mask) {
  std::cout << "Toggle " << std::dec << pos << ": "
            << std::hex << std::setw(8) << (bits ^ mask)
            << std::endl;
}

int main(int argc, char *argv[]) {
  std::cout << std::hex << std::setfill('0');
  do_negate("red", RED);
  do_negate("white", WHITE);
  do_and("red&white", RED, WHITE);
  do_or("red|white", RED, WHITE);

  do_negate("mask", MASK);
  do_xor("mask^red", MASK, RED);
  do_xor("mask^white", MASK, WHITE);

  do_negate("flags", FLAGS);
  get_bit(FLAGS, 1, BIT1);
  get_bit(FLAGS, 6, BIT6);
  get_bit(FLAGS, 20, BIT20);

  set_off(FLAGS, 1, BIT1);
  set_on(FLAGS, 20, BIT20);
  set_toggle(FLAGS, 6, BIT6);

  return 0;
}
