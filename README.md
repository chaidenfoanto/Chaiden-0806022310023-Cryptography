# Sistem Kriptografi Sederhana dengan XOR dan Base64

Ini adalah implementasi sederhana dari sistem kriptografi menggunakan operasi XOR dengan empat binary keys yang dihasilkan secara acak berdasarkan *secret key*. Ciphertext yang dihasilkan kemudian di-*encode* ke dalam format Base64 untuk memudahkan penyimpanan dan transmisi.

## Fitur

- **Enkripsi**: Mengenkripsi teks menggunakan operasi XOR dengan empat kunci binary acak yang dihasilkan dari *secret key*.
- **Dekripsi**: Mengembalikan teks asli dari ciphertext yang dienkripsi.
- **Base64 Encoding**: Ciphertext di-*encode* dalam format Base64 agar mudah dibaca dan disimpan.

## Prasyarat

Pastikan kamu telah menginstal **Python** versi 3.x di sistemmu.

## Instalasi

1. Clone repositori ini ke mesin lokalmu menggunakan perintah berikut:
   ```bash
   git clone https://github.com/chaidenfoanto/Chaiden-0806022310023-Cryptography.git
    ```
2. Masuk ke direktori proyek:
  ```bash
    cd Chaiden-0806022310023-Cryptography
  ```
3. Jalankan skrip cryptography.py dengan Python:
  ```bash
    python3 cryptographic.py
  ```

## Cara Penggunaan

1. Di dalam file cryptography.py, kamu bisa mengubah nilai variabel secret_key dan plaintext untuk mengenkripsi teks baru. Berikut contoh dari file tersebut:
   ```python
    secret_key = "rahasia123"
    plaintext = "Apa kabar?"
    
    cipher = Cryptography(secret_key)
    ciphertext = cipher.encrypt(plaintext)
    print(f"Ciphertext (base64): {ciphertext}")
    
    decrypted_text = cipher.decrypt(ciphertext)
    print(f"Decrypted Text: {decrypted_text}")
   ```
2. Setelah menjalankan perintah di atas, kamu akan melihat hasil enkripsi dan dekripsi:
  ```bash
    Plaintext: Apa kabar?
    Ciphertext (base64): Lx4PTgUPDA8cUQ==
    Decrypted Text: Apa kabar?
  ```

## Penjelasan Kode

- **generate_keys()**: Fungsi ini menghasilkan empat binary keys (B1, B2, B3, B4) menggunakan nilai acak yang diperoleh dari secret key. Binary keys ini digunakan untuk mengenkripsi setiap karakter plaintext.
- **encrypt(plaintext)**: Fungsi ini mengenkripsi plaintext dengan cara mengubah setiap karakter menjadi nilai ASCII, kemudian melakukan XOR dengan keempat binary keys secara berurutan. Hasilnya kemudian dikonversi ke format Base64 untuk output.
- **decrypt(ciphertext)**: Fungsi ini mendekripsi ciphertext yang sudah di-encode dalam Base64. Setiap nilai dienkripsi dengan cara membalik proses XOR menggunakan binary keys yang sama, dan akhirnya dikonversi kembali ke plaintext.

