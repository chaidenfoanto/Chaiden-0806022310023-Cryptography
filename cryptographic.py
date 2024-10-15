import random
import base64

class Cryptography:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    # Fungsi untuk menghasilkan binary keys B1, B2, B3, dan B4 dari secret_key
    def generate_keys(self):
        random.seed(self.secret_key)  # Menggunakan secret_key untuk menyusun seed random
        B1 = random.randint(0, 255)  # Menghasilkan key acak antara 0-255
        B2 = random.randint(0, 255)  # Menghasilkan key acak antara 0-255
        B3 = random.randint(0, 255)  # Menghasilkan key acak antara 0-255
        B4 = random.randint(0, 255)  # Menghasilkan key acak antara 0-255
        return B1, B2, B3, B4

    # Fungsi enkripsi
    def encrypt(self, plaintext):
        B1, B2, B3, B4 = self.generate_keys()  # Menghasilkan binary keys
        ciphertext = []  # List untuk menyimpan ciphertext dalam bentuk integer
        for char in plaintext:
            ascii_value = ord(char)  # Mengonversi karakter menjadi nilai ASCII
            encrypted_value = ascii_value ^ B1 ^ B2 ^ B3 ^ B4  # Melakukan operasi XOR
            ciphertext.append(encrypted_value)  # Menyimpan nilai terenkripsi ke dalam list
        # Mengonversi ciphertext menjadi bytes dan kemudian mengencode dengan base64
        return base64.b64encode(bytearray(ciphertext)).decode('utf-8')  # Mengembalikan ciphertext dalam bentuk string

    # Fungsi dekripsi
    def decrypt(self, ciphertext):
        B1, B2, B3, B4 = self.generate_keys()  # Menghasilkan binary keys
        decoded_bytes = base64.b64decode(ciphertext)  # Decode dari base64 ke bytes
        plaintext = ""  # String untuk menyimpan plaintext
        for encrypted_value in decoded_bytes:
            ascii_value = encrypted_value ^ B1 ^ B2 ^ B3 ^ B4  # Melakukan operasi XOR untuk mendapatkan nilai ASCII asli
            plaintext += chr(ascii_value)  # Mengonversi nilai ASCII kembali menjadi karakter
        return plaintext  # Mengembalikan plaintext

# Contoh penggunaan
if __name__ == "__main__":
    secret_key = "rahasia123"  # Secret key yang lebih kompleks
    plaintext = "Apa kabar?"  # Plaintext yang akan dienkripsi
    
    cipher = Cryptography(secret_key)  # Membuat objek dari Cryptography
    print(f"Plaintext: {plaintext}")
    ciphertext = cipher.encrypt(plaintext)  # Enkripsi plaintext
    print(f"Ciphertext (base64): {ciphertext}")  # Menampilkan ciphertext dalam bentuk base64
    decrypted_text = cipher.decrypt(ciphertext)  # Dekripsi ciphertext
    print(f"Decrypted Text: {decrypted_text}")  # Menampilkan plaintext hasil dekripsi
