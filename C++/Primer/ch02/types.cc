/**
 * Describe the C++ builtin types.
*/

#include <iomanip>
#include <iostream>
#include <limits>

void show_headers(void) {
    std::cout << std::setw(10) << std::left << "type"
        << std::setw(6) << std::right << "size"
        << std::setw(8) << "digits"
        << std::setw(8) << "signed"
        << std::setw(24) << "min"
        << std::setw(24) << "lowest"
        << std::setw(24) << "max"
        << std::endl;
    std::cout << std::setw(10) << std::left << "----"
        << std::setw(6) << std::right << "----"
        << std::setw(8) << "------"
        << std::setw(8) << "------"
        << std::setw(24) << "---"
        << std::setw(24) << "------"
        << std::setw(24) << "---"
        << std::endl;
}

template <typename T, typename U>
void show_type(const std::string &name) {
    std::cout << std::setw(10) << std::left << name
        << std::setw(6) << std::right << sizeof(T)
        << std::setw(8) << std::numeric_limits<T>::digits
        << std::setw(8) << std::numeric_limits<T>::is_signed
        << std::setw(24) << static_cast<U>(std::numeric_limits<T>::min())
        << std::setw(24) << static_cast<U>(std::numeric_limits<T>::lowest())
        << std::setw(24) << static_cast<U>(std::numeric_limits<T>::max())
        << std::endl;
}

int main(int argc, char *argv[]) {
    show_headers();
    show_type<bool, bool>("bool");
    show_type<char, int>("char");
    show_type<signed char, int>("schar");
    show_type<unsigned char, unsigned int>("uchar");
    show_type<wchar_t, wchar_t>("wchar_t");
    show_type<char16_t, char16_t>("char16_t");
    show_type<char32_t, char32_t>("char32_t");
    show_type<short, short>("short");
    show_type<unsigned short, unsigned short>("ushort");
    show_type<int, int>("int");
    show_type<unsigned int, unsigned int>("uint");
    show_type<long, long>("long");
    show_type<unsigned long, unsigned long>("ulong");
    show_type<long long, long long>("llong");
    show_type<unsigned long long, unsigned long long>("ullong");
    show_type<float, float>("float");
    show_type<double, double>("double");
    show_type<long double, long double>("ldouble");

    return 0;
}
