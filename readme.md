# Diffie Helman dan Vigenere Chiper

Repository ini berisi source code dari program python untuk melakukan enkripsi dan dekripsi teks menggunakan algoritma Vigenere chiper dan Diffie Hellman untuk melakukan pertukaran kunci.

### Diffie Hellman
Pertukaran kunci Diffie Hellman merupakan metode untuk melakukan pertukaran kunci kriptografi secara aman oleh dua pihak melalui channel yang bersifat public. Berikut adalah cara kerja Algoritma Diffie hellman :

* Misalkan Alice dan Bob adalah pihak-pihak
yang berkomunikasi. Mula-mula Alice dan
Bob menyepakati 2 buah bilangan yang
besar (sebaiknya prima) P dan Q, sedemikian
sehingga P < Q. Nilai P dan Q tidak perlu
rahasia, bahakan Alice dan Bob dapat
membicarakannya melalui saluran yang tidak
aman sekalipun. 

* Alice membangkitkan bilangan bulat acak x
yang besar dan mengirim hasil perhitungan
berikut kepada Bob :
X = P^x mod Q. 

* Bob membangkitkan bilangan bulat acak y
yang besar dan mengirim hasil perhitungan
berikut kepada Alice:
Y = P^y mod Q. 

* Alice menghitung
K = Y^x mod Q.

* Bob menghitung
K’ = X^y mod Q. 

* Jika perhitungan dilakukan dengan benar maka K
= K’. Dengan demikian Alice dan Bob telah
memiliki sebuah kunci yang sama tanpa diketahui
pihak lain.

Agar algoritma tersebut aman, maka diperlukan bilangan prima yang sangat besar sehingga dalam program ini terdapat algoritma pembangkitan bilangan prima yang mengimplementasikan algoritma Miller Rabin Primality Test untuk membangkitkan bilangan prima sebesar 128-bit.

### Vigenere Chiper
Vigenere Chiper merupakan algoritma kriptografi kunci simetri yang menyandikan teks alfabet dengan menggunakan deretan algoritma Caesar Chiper berdasarkan huruf-huruf pada kata kunci. kelebihan algoritma ini dibanding algoritma Caesar Chiper, algoritma ini aman dari serangan Frequency Analysis. notasi algoritmik yang digunakan untuk mengenkripsi suatu karakter alphabet plaintext (P) menjadi ciphertext (C) dengan kunci K adalah sebagai berikut :
* Ci = (Pi + Ki) MOD 26

Sedangkan untuk dekripsi suatu karakter adalah sebagai berikut :
* Pi = (Ci - Ki) MOD 26