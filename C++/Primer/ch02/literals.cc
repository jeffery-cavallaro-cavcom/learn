// Various Literal Forms

#include <iostream>

int main(int argc, char *argv[]) {
    // Radices:
    std::cout << "Decimal: " << 100 << std::endl;
    std::cout << "Octal: " << 0144 << std::endl;
    std::cout << "Hex: " << 0x64 << std::endl;

    // Modifiers:
    std::cout << "int: " << sizeof(1) << std::endl;
    std::cout << "uint: " << sizeof(1u) << std::endl;
    std::cout << "long: " << sizeof(1L) << std::endl;
    std::cout << "ulong: " << sizeof(1uL) << std::endl;
    std::cout << "llong: " << sizeof(1LL) << std::endl;
    std::cout << "ullong: " << sizeof(1uLL) << std::endl;

    // The '-' is an operator, not part of the value:
    std::cout << -256u << std::endl;  // 4294967040

    // Forms:
    std::cout << 3.14 << std::endl;
    std::cout << 314e-2 << std::endl;
    std::cout << 0.00314e3 << std::endl;

    // Modifiers:
    std::cout << "float: " << sizeof(1.0f) << std::endl;
    std::cout << "double: " << sizeof(1.0) << std::endl;
    std::cout << "ldouble: " << sizeof(1.0L) << std::endl;

    // Character vs String:
    std::cout << sizeof('A') << std::endl;  // 1
    std::cout << sizeof("A") << std::endl;  // 2 (A\0)

    // String concatenation (note that literals are const char *):
    const char *message =
        "Hello, "
        "World "
        "!!!";
    std::cout << message << std::endl;

    return 0;
}
