/**
 * Tests whether a temporary object is properly destroyed.
*/

#include <iostream>

class A {
 public:
    explicit A(int v): a_(v) {
        std::cout << "A constructor: " << a_ << std::endl;
    }
    ~A(void) {
        std::cout << "A destructor: " << a_ << std::endl;
    }
 private:
    int a_;
};

class B {
 public:
    explicit B(int v): b_(v) {
        std::cout << "B constructor: " << b_ << std::endl;
    }
    ~B(void) {
        std::cout << "B destructor: " << b_ << std::endl;
    }
    operator A() {
        return A(b_ + 1);
    }
 private:
    int b_;
};


int main(int argc, char *argv[]) {
    B b(100);
    const A &a = b;
    return 0;
}
