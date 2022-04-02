# Tugas Kecil 3 IF2211 Strategi Algoritma
## Garis Besar Program
Permasalahan 15-Puzzle adalah sebuah permainan di petak berukuran 4x4 dimana 15 kotak diantaranya berisi ubin dengan angka 1-15 yang bisa digeser-geser. Sedangkan 1 kotak lainnya tidak terisi oleh ubin apapun. Untuk setiap giliran permainan, pemain bisa memilih ingin menggeser ubin yang mana ke arah mana. Perlu diingat bahwa ubin yang bisa digeser hanyalah ubin yang bersebelahan dengan kotak yang tidak terisi oleh ubin apapun.
Permasalahan ini bisa diselesaikan dengan algoritma branch and bound yang serupa dengan algoritma breadth first search (bfs) hanya saja untuk mengelola antrian simpul yang akan dikunjungi digunakan struktur data priority queue yang menggunakan cost dari suatu simpul sebagai prioritasnya. Semakin kecil cost dari suatu simpul, maka simpul tersebut akan lebih diprioritaskan.

## Prasyarat Program
Untuk menjalankan program ini, pengguna harus menginstall Python 3.X

## Cara Menggunakan Program
Masuk ke direktori utama repository ini lalu jalankan perintah berikut (ganti py dengan python3 bila menggunakan Linux)
```
py src/main.py
```
Berikan informasi yang diminta oleh program. Berikut adalah contoh keberjalanan program bila menggunakan puzzle yang dibangkitkan secara random
```
Ketik 1 untuk menggunakan puzzle random, ketik 2 untuk menggunakan puzzle dari file : 1
Ketik level puzzle yang diinginkan (1, 2, atau 3) : 1
PUZZLE AWAL
=====================
*    | 2  | 3  | 4  *
*-------------------*
* 1  | 5  | 6  | 8  *
*-------------------*
* 9  | 13 | 7  | 12 *
*-------------------*
* 14 | 10 | 11 | 15 *
=====================
Nilai KURANG(1)=0
Nilai KURANG(2)=1
Nilai KURANG(3)=1
Nilai KURANG(4)=1
Nilai KURANG(5)=0
Nilai KURANG(6)=0
Nilai KURANG(7)=0
Nilai KURANG(8)=1
Nilai KURANG(9)=1
Nilai KURANG(10)=0
Nilai KURANG(11)=0
Nilai KURANG(12)=2
Nilai KURANG(13)=4
Nilai KURANG(14)=2
Nilai KURANG(15)=0
Nilai KURANG(16)=15
Jumlah dari KURANG(i) ditambah X : 28
Puzzle dapat diselesaikan !
Mencari solusi...
Tekan ENTER untuk memulai animasi
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
* 5  | 6  | 7  | 8  *
*-------------------*
* 9  | 10 | 11 | 12 *
*-------------------*
* 13 | 14 | 15 |    *
=====================
Ingin mencetak semua langkah (y/n) ? y
=====================
*    | 2  | 3  | 4  *
*-------------------*
* 1  | 5  | 6  | 8  *
*-------------------*
* 9  | 13 | 7  | 12 *
*-------------------*
* 14 | 10 | 11 | 15 *
=====================
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
*    | 5  | 6  | 8  *
*-------------------*
* 9  | 13 | 7  | 12 *
*-------------------*
* 14 | 10 | 11 | 15 *
=====================
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
* 9  | 5  | 6  | 8  *
*-------------------*
*    | 13 | 7  | 12 *
*-------------------*
* 14 | 10 | 11 | 15 *
=====================
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
* 9  | 5  | 6  | 8  *
*-------------------*
* 13 |    | 7  | 12 *
*-------------------*
* 14 | 10 | 11 | 15 *
=====================
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
* 9  | 5  | 6  | 8  *
*-------------------*
* 13 | 10 | 7  | 12 *
*-------------------*
* 14 |    | 11 | 15 *
=====================
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
* 9  | 5  | 6  | 8  *
*-------------------*
* 13 | 10 | 7  | 12 *
*-------------------*
*    | 14 | 11 | 15 *
=====================
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
* 9  | 5  | 6  | 8  *
*-------------------*
*    | 10 | 7  | 12 *
*-------------------*
* 13 | 14 | 11 | 15 *
=====================
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
*    | 5  | 6  | 8  *
*-------------------*
* 9  | 10 | 7  | 12 *
*-------------------*
* 13 | 14 | 11 | 15 *
=====================
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
* 5  |    | 6  | 8  *
*-------------------*
* 9  | 10 | 7  | 12 *
*-------------------*
* 13 | 14 | 11 | 15 *
=====================
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
* 5  | 6  |    | 8  *
*-------------------*
* 9  | 10 | 7  | 12 *
*-------------------*
* 13 | 14 | 11 | 15 *
=====================
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
* 5  | 6  | 7  | 8  *
*-------------------*
* 9  | 10 |    | 12 *
*-------------------*
* 13 | 14 | 11 | 15 *
=====================
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
* 5  | 6  | 7  | 8  *
*-------------------*
* 9  | 10 | 11 | 12 *
*-------------------*
* 13 | 14 |    | 15 *
=====================
=====================
* 1  | 2  | 3  | 4  *
*-------------------*
* 5  | 6  | 7  | 8  *
*-------------------*
* 9  | 10 | 11 | 12 *
*-------------------*
* 13 | 14 | 15 |    *
=====================
Jumlah node yang dibangkitkan :  175
Waktu yang dibutuhkan :  0.007813215255737305  detik
```
## Aturan File Input
1. Semua file input diletakkan di folder test
2. File input terdiri atas empat baris yang diakhiri oleh sebuah newline
3. Setiap baris terdiri dari empat buah angka yang dipisahkan oleh spasi
4. Hanya boleh ada angka 1-16 dengan 16 mewakili ubin kosong
5. Diasumsikan tidak ada angka yang tertulis dua kali
