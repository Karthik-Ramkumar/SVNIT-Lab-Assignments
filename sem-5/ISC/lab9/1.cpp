#include <iostream>
#include <random>
#include <cstdint>
#include <iomanip>

// =============================================================================
// Section 1: Modular Arithmetic Functions
// =============================================================================

/**
 * Safe modular multiplication: (a * b) % mod
 * Uses a 128-bit unsigned integer to prevent 64-bit integer overflow during
 * the intermediate multiplication step before taking the modulus.
 */
uint64_t mod_mul(uint64_t a, uint64_t b, uint64_t mod) {
#if defined(__SIZEOF_INT128__)
    return static_cast<uint64_t>((static_cast<unsigned __int128>(a) * b) % mod);
#else
    // Fallback binary modular multiplication if 128-bit types are unavailable
    uint64_t res = 0;
    a %= mod;
    while (b > 0) {
        if (b & 1) res = (res + a) % mod;
        a = (2 * a) % mod;
        b >>= 1;
    }
    return res;
#endif
}

/**
 * Modular exponentiation using repeated squaring (binary exponentiation):
 * Computes (base^exp) % mod in O(log exp) time without using floating-point pow().
 */
uint64_t mod_exp(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) {
            result = mod_mul(result, base, mod);
        }
        base = mod_mul(base, base, mod);
        exp >>= 1;
    }
    return result;
}

// =============================================================================
// Section 2: Cryptographic Domain Parameters (Prime modulus p & Generator g)
// =============================================================================
// p: Safe prime modulus (2^31 - 1, 8th Mersenne prime)
// g: Primitive root / generator modulo p
const uint64_t P = 2147483647ULL;
const uint64_t G = 7ULL;

int main() {
    std::cout << "========================================================\n";
    std::cout << "   Lab 10: Diffie-Hellman Key Exchange Implementation   \n";
    std::cout << "========================================================\n\n";

    // Display Public Domain Parameters
    std::cout << "[+] Public Domain Parameters:\n";
    std::cout << "    Prime modulus (p) : " << P << "\n";
    std::cout << "    Generator     (g) : " << G << "\n\n";

    // =========================================================================
    // Section 3: Random Private Key Generation (Alice & Bob)
    // =========================================================================
    // Chosen securely from the range [2, p - 2] using 64-bit Mersenne Twister
    std::random_device rd;
    std::mt19937_64 gen(rd());
    std::uniform_int_distribution<uint64_t> dist(2, P - 2);

    uint64_t a = dist(gen); // Alice's private key
    uint64_t b = dist(gen); // Bob's private key

    std::cout << "[+] Step 1: Private Key Generation:\n";
    std::cout << "    Alice's Private Key (a) : " << a << "\n";
    std::cout << "    Bob's Private Key   (b) : " << b << "\n\n";

    // =========================================================================
    // Section 4: Public Key Computation
    // =========================================================================
    // Alice computes: A = (g^a) mod p
    // Bob computes  : B = (g^b) mod p
    uint64_t A = mod_exp(G, a, P);
    uint64_t B = mod_exp(G, b, P);

    std::cout << "[+] Step 2: Public Key Computation:\n";
    std::cout << "    Alice's Public Key (A = g^a mod p) : " << A << "\n";
    std::cout << "    Bob's Public Key   (B = g^b mod p) : " << B << "\n\n";

    // Exchange Simulation
    std::cout << "[+] Step 3: Public Key Exchange:\n";
    std::cout << "    Alice sends public key A (" << A << ") to Bob.\n";
    std::cout << "    Bob sends public key B (" << B << ") to Alice.\n\n";

    // =========================================================================
    // Section 5: Shared Secret Key Calculation
    // =========================================================================
    // Alice computes: K_Alice = (B^a) mod p
    // Bob computes  : K_Bob   = (A^b) mod p
    uint64_t shared_secret_Alice = mod_exp(B, a, P);
    uint64_t shared_secret_Bob   = mod_exp(A, b, P);

    std::cout << "[+] Step 4: Shared Secret Calculation:\n";
    std::cout << "    Alice computes: K_Alice = (B^a mod p) = " << shared_secret_Alice << "\n";
    std::cout << "    Bob computes  : K_Bob   = (A^b mod p) = " << shared_secret_Bob << "\n\n";

    // =========================================================================
    // Section 6: Verification
    // =========================================================================
    std::cout << "[+] Step 5: Verification:\n";
    if (shared_secret_Alice == shared_secret_Bob) {
        std::cout << "    [SUCCESS] Both shared secret keys match!\n";
        std::cout << "    Established Shared Key: " << shared_secret_Alice << "\n";
    } else {
        std::cout << "    [FAILURE] Shared secret keys do not match!\n";
    }
    std::cout << "========================================================\n";

    return 0;
}
