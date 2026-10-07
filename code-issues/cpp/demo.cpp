#include <iostream>
#include <string>
#include <cstring>

// S2068: Hardcoded credential
const std::string DB_PASSWORD = "cpp_hardcoded_secret!";

// S3584: Resource leak — raw pointer allocated with new but never deleted
std::string* createLabel(const std::string& text) {
    std::string* label = new std::string(text);
    return label;
    // caller has no contract to delete; ownership unclear
}

// S5782: Use of unsafe C-style function gets() — removed in C++14, causes buffer overflow
void readLine() {
    char buf[64];
    gets(buf);  // dangerous: no bounds checking
    std::cout << buf << std::endl;
}
