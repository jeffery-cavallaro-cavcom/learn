// Various Literal Forms

#include <iostream>
#include <locale>

template<class Facet>
struct DeletableFacet : Facet {
    template <class ...Args>
    explicit DeletableFacet(Args&& ...args)
        : Facet(std::forward<Args>(args)...) {}

    ~DeletableFacet(void) {}
};

template <class W, class N>
N encode(W in) {
    std::wstring_convert<
        DeletableFacet<std::codecvt<typename W::value_type,
                                    typename N::value_type,
                                    std::mbstate_t>>,
        typename W::value_type
        > converter("Conversion error");
    return converter.to_bytes(in);
}

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
    std::cout << "char: " << sizeof('A') << std::endl;  // 1
    std::cout << "wchar_t: " << sizeof(L'A') << std::endl;  // 4
    std::cout << "utf8: " << sizeof(u8'A') << std::endl;  // 1
    std::cout << "utf16: " << sizeof(u'A') << std::endl;  // 2
    std::cout << "uft32: " << sizeof(U'A') << std::endl;  // 4
    std::cout << "string: " << sizeof("A") << std::endl;  // 2
    std::cout << "wstring: " << sizeof(L"A") << std::endl;  // 8
    std::cout << "u8string: " << sizeof(u8"A") << std::endl;  // 2
    std::cout << "u16string: " << sizeof(u"A") << std::endl;  // 4
    std::cout << "u32string: " << sizeof(U"A") << std::endl;  // 8

    // String concatenation (note that literals are const char *):
    const char *message =
        "Hello, "
        "World "
        "!!!";
    std::cout << message << std::endl;

    // Escapes:
    std::cout << "A \"\t\" tab in double quotes" << std::endl;
    std::cout << "A\102\x43" << std::endl;

    // String Encodings:
    const char s1[] = "\xC2\xA1Hasta Ma\xC3\xB1""ana!";
    std::cout << sizeof(s1) << ": " << s1 << std::endl;

    const char s2[] = "\u00A1Hasta Ma\u00F1""ana!";
    std::cout << sizeof(s2) << ": " << s2 << std::endl;

    const char16_t s3[] = u"\u00A1Hasta Ma\u00F1""ana!";
    std::u16string ss3(s3);
    std::string ns3 = encode<std::u16string, std::string>(ss3);
    std::cout << sizeof(s3) << ": " <<  ns3 << std::endl;

    const char32_t s4[] = U"\u00A1Hasta Ma\u00F1""ana!";
    std::u32string ss4(s4);
    std::string ns4 = encode<std::u32string, std::string>(ss4);
    std::cout << sizeof(s4) << ": " <<  ns4 << std::endl;

    return 0;
}
