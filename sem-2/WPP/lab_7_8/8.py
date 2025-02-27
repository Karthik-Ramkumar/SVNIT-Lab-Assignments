def decode_message(encoded_message):
    def _decode(index, current_decoding):
        if index == len(encoded_message):
            result.append(current_decoding)
            return

        if encoded_message[index] == '0': #handle leading 0s
          return

        # Try decoding one digit
        digit = int(encoded_message[index])
        if 1 <= digit <= 26:
            _decode(index + 1, current_decoding + chr(digit + 64))  # 64 is ASCII for 'A'

        # Try decoding two digits
        if index + 1 < len(encoded_message):
            two_digits = int(encoded_message[index:index+2])
            if 10 <= two_digits <= 26:
                _decode(index + 2, current_decoding + chr(two_digits + 64))

    result = []
    _decode(0, "")
    return result

encoded_message = "11106"
decoded_messages = decode_message(encoded_message)
print(decoded_messages)  

encoded_message = "226"
decoded_messages = decode_message(encoded_message)
print(decoded_messages) 

encoded_message = "06" 
decoded_messages = decode_message(encoded_message)
print(decoded_messages)
encoded_message = "10" 
decoded_messages = decode_message(encoded_message)
print(decoded_messages) 