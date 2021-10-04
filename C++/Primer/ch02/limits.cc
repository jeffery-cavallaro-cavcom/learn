#include <iostream>
#include <limits>
#include <string>

template <typename T>
void show_numeric(const std::string &name) {
    using type = std::numeric_limits<T>;
    std::cout << name << ":"
              << " size=" << sizeof(T)
              << " signed=" << type::is_signed
              << " integer=" << type::is_integer
              << " min=" << type::min()
              << " max=" << type::max()
              << std::endl;
}

template <typename T>
void show_character(const std::string &name) {
    using type = std::numeric_limits<T>;
    std::cout << name << ":"
              << " size=" << sizeof(T)
              << " signed=" << type::is_signed
              << " integer=" << type::is_integer;
    if (type::is_signed) {
        std::cout << " min=" << static_cast<long>(type::min())
                  << " max=" << static_cast<long>(type::max());
    } else {
        std::cout << " min=" << static_cast<ulong>(type::min())
                  << " max=" << static_cast<ulong>(type::max());
    }
    std::cout << std::endl;
}

int main(int argc, char *argv[]) {
    show_numeric<bool>("bool");

    show_numeric<short>("short");
    show_numeric<unsigned short>("ushort");
    show_numeric<int>("int");
    show_numeric<unsigned int>("uint");
    show_numeric<long>("long");
    show_numeric<unsigned long>("ulong");
    show_numeric<long long>("llong");
    show_numeric<unsigned long long>("ullong");

    show_character<char>("char");
    show_character<signed char>("schar");
    show_character<unsigned char>("uchar");
    show_character<wchar_t>("wchar_t");
    show_character<char16_t>("char16_t");
    show_character<char32_t>("char32_t");

    show_numeric<float>("float");
    show_numeric<double>("double");
    show_numeric<long double>("ldouble");

    return 0;
}
