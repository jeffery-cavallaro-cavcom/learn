/**
 * Demonstrates the different character types and how to output them.
*/

#include <iomanip>
#include <iostream>
#include <locale>
#include <string>

void show_bytes(const void *value, std::size_t length) {
    const unsigned char *bytes = reinterpret_cast<const unsigned char *>(value);
    for (unsigned int ui = 0; ui < length; ++ui) {
        if ((ui % 16) == 0) {
            std::cout << std::endl;
        } else {
            std::cout << ' ';
        }
        unsigned int uc = bytes[ui];
        std::cout << std::hex << std::setw(2) << std::setfill('0') << uc;
    }
    std::cout << std::endl;
}

template <typename T>
void show_string(const T *data, std::size_t size) {
    mbstate_t mb;
    char buffer[256];
    char *to_next;

    auto &converter =
        std::use_facet<std::codecvt<T, char, std::mbstate_t>>(std::locale());
    const T *from_next;
    std::size_t n = size / sizeof(T);
    converter.out(
        mb,
        data, data + n, from_next,
        buffer, buffer + sizeof(buffer), to_next
    );
    *to_next = '\0';
    std::cout << buffer << std::endl;
}

int main(int argc, char *argv[]) {
    std::cout << "\nchar: ";
    const char c[] ="\xC2\xA1Hasta ma\xC3\xb1\x61na!";
    std::cout << c << std::endl;
    show_bytes(c, sizeof(c));

    std::cout << "\nchar16_t: ";
    const char16_t u16c[] = u"\u00A1Hasta ma\u00F1ana!";
    show_string(u16c, sizeof(u16c));
    show_bytes(u16c, sizeof(u16c));

    std::cout << "\nchar32_t: ";
    const char32_t u32c[] = U"\u00A1Hasta ma\u00F1ana!";
    show_string(u32c, sizeof(u32c));
    show_bytes(u32c, sizeof(u32c));

    std::cout << "\nwchar_t: ";
    const wchar_t wc[] = L"Hasta manana!";
    std::wcout << wc << std::endl;
    show_bytes(wc, sizeof(wc));

    return 0;
}
