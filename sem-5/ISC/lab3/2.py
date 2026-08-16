import string

KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"

def encrypt(text):
    alphabet = string.ascii_uppercase
    result = ""

    for char in text.upper():
        if char.isalpha():
            result += KEY[alphabet.index(char)]
        else:
            result += char

    return result


def decrypt(text):
    alphabet = string.ascii_uppercase
    result = ""

    for char in text.upper():
        if char.isalpha():
            result += alphabet[KEY.index(char)]
        else:
            result += char

    return result


patient_id = "PATIENT-5465"
diagnostic_note = "PATIENT HAS SEVERE FEVER"

encrypted_id = encrypt(patient_id)
encrypted_note = encrypt(diagnostic_note)

print("Encrypted ID:", encrypted_id)
print("Encrypted Note:", encrypted_note)

print("Decrypted ID:", decrypt(encrypted_id))
print("Decrypted Note:", decrypt(encrypted_note))