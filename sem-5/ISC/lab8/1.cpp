#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using namespace std;

struct EG {
    cpp_int g, x, y;
};

EG egcd(cpp_int a, cpp_int b) {
    if (b == 0)
        return {a, 1, 0};

    EG t = egcd(b, a % b);
    return {t.g, t.y, t.x - (a / b) * t.y};
}

cpp_int modinv(cpp_int a, cpp_int m) {
    auto t = egcd(a, m);
    if (t.g != 1)
        throw runtime_error("Modular inverse does not exist");

    return (t.x % m + m) % m;
}

cpp_int modexp(cpp_int base, cpp_int exp, const cpp_int& mod) {
    base %= mod;
    cpp_int res = 1;

    while (exp > 0) {
        if (exp % 2 == 1)
            res = (res * base) % mod;

        base = (base * base) % mod;
        exp /= 2;
    }

    return res;
}

int main() {
    cout << "=== RSA Implementation (Toy Example) ===\n";

    // Key Generation
    cpp_int p = 61, q = 53;
    cpp_int n = p * q;
    cpp_int phi = (p - 1) * (q - 1);
    cpp_int e = 17;
    cpp_int d = modinv(e, phi);

    cout << "p = " << p << "\nq = " << q << "\n";
    cout << "n = " << n << "\nphi(n) = " << phi << "\n";
    cout << "Public exponent e = " << e
         << "\nPrivate exponent d = " << d << "\n";

    // Encrypt & Decrypt
    cpp_int m = 65;
    cpp_int c = modexp(m, e, n);
    cpp_int m_dec = modexp(c, d, n);

    cout << "\nMessage m = " << m;
    cout << "\nCiphertext c = " << c;
    cout << "\nDecrypted message m_dec = " << m_dec << "\n";

    if (m == m_dec)
        cout << "\n[OK] Decryption successful!\n";
    else
        cout << "\n[ERROR] Decryption failed!\n";

    return 0;
}