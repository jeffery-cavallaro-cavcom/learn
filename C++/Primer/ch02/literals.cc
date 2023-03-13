/**
 * Demonstrates the use of literals.
*/

#include <iostream>

int main(int argc, char *argv[]) {
    // Integer values.
    std::cout << "Binary 0b01100100: " << 0b01100100 << std::endl;
    std::cout << "Octal 0144: " << 0144 << std::endl;
    std::cout << "Decimal 100: " << 100 << std::endl;
    std::cout << "Hex 0x64: " << 0x64 << std::endl;

    // Floating point values.
    std::cout << "3.14 = " << 3.14 << std::endl;
    std::cout << "0.0314e2 = " << 0.0314e2 << std::endl;
    std::cout << "314.0e-2 = " << 314.0e-2 << std::endl;

    // Autosizing.  Signed values are int, long, or llong.
    std::cout << "size of 2,000,000,000: " << sizeof(2000000000) << std::endl;
    std::cout << "size of 4,000,000,000: " << sizeof(4000000000) << std::endl;
    std::cout << "size of 9000000000000000000: "
        << sizeof(9000000000000000000) << std::endl;

    // Octal and hex values are int, uint, long, ulong, llong, or ullong.
    std::cout << "size of " << 0x7FFFFFFF << ": "
        << sizeof(0x7FFFFFFF) << std::endl;
    std::cout << "size of " << 0x80000000 << ": "
        << sizeof(0x80000000) << std::endl;
    std::cout << "size of " << 0x7FFFFFFFFFFFFFFF << ": "
        << sizeof(0x7FFFFFFFFFFFFFFF) << std::endl;
    std::cout << "size of " << 0x8000000000000000 << ": "
        << sizeof(0x8000000000000000) << std::endl;

    // Suffixes.
    std::cout << "size of 10: " << sizeof(10) << std::endl;
    std::cout << "size of 10u: " << sizeof(10) << std::endl;
    std::cout << "size of 10L: " << sizeof(10L) << std::endl;
    std::cout << "size of 10uL: " << sizeof(10uL) << std::endl;
    std::cout << "size of 10LL: " << sizeof(10LL) << std::endl;
    std::cout << "size of 10uLL: " << sizeof(10uLL) << std::endl;

    std::cout << "size of 3.14: " << sizeof(3.14) << std::endl;
    std::cout << "size of 3.14F: " << sizeof(3.14F) << std::endl;
    std::cout << "size of 3.14L: " << sizeof(3.14L) << std::endl;

    // Characters and strings:
    std::cout << "This is a string value: " << "Hello, World !!!" << std::endl;
    std::cout << "This is a character value: " << 'a' << std::endl;
    std::cout << "Normal escapes: " << "\"\'\?\\" << std::endl;
    std::cout << "This is a concatenated string: "
        "Here is the next part." << std::endl;

    // Prefixes:
    std::cout << "Size of 'a': " << sizeof('a') << std::endl;
    std::cout << "Size of L'a': " << sizeof(L'a') << std::endl;
    std::cout << "Size of u'a': " << sizeof(u'a') << std::endl;
    std::cout << "Size of U'a': " << sizeof(U'a') << std::endl;
    std::cout << "Size of u8'a': " << sizeof(u8'a') << std::endl;

    std::cout << "Size of \"a\": " << sizeof("a") << std::endl;
    std::cout << "Size of L\"a\": " << sizeof(L"a") << std::endl;
    std::cout << "Size of u\"a\": " << sizeof(u"a") << std::endl;
    std::cout << "Size of U\"a\": " << sizeof(U"a") << std::endl;
    std::cout << "Size of u8\"a\": " << sizeof(u8"a") << std::endl;

    // Booleans:
    std::cout << std::noboolalpha << true << std::endl;
    std::cout << std::boolalpha << true << std::endl;

    std::cout << std::noboolalpha << false << std::endl;
    std::cout << std::boolalpha << false << std::endl;

    return 0;
}
