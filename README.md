# Stima-Convex-Hull
## Deskripsi singkat
Algoritma pencarian convex hull dengan strategi divide and conquer. Diimplementasikan dalam bahasa Python.
## Struktur
- bryanhull.py: Implementasi algoritma dalam kelas ConvexHull
- main.ipynb: Contoh demonstrasi dan visualisasi
- line.py, utils.py, bryanhull_test.py: Modul pendukung dan tes
## Requirement
Algoritma utama, bryanhull.py, tidak memerlukan instalasi modul tambahan dari luar karena menggunakan List bawaan Python. <br>
Untuk program utama, main.ipynb, memerlukan instalasi modul numpy, pandas, matplotlib, sklearn, dan scipy. Juga memerlukan Jupyter Notebook atau sejenisnya untuk menjalankan.
## Langkah Penggunaan
Pada bryanhull.py, kelas ConvexHull digunakan untuk mencari convex hull. Kelas memerlukan masukan daftar titik List of List[2]: [[x1, y1], [x2, y2], ..., [xn, yn]]. Jika masukan berupa data dalam format array numpy, perlu diubah ke List Python dengan arr.tolist(). Kelas langsung melakukan perhitungan ketika instantiasi dan menyimpan hasilnya ke atribut convexhullpoints (daftar titik convex hull) dan simplices (pasangan indeks titik jalur convex hull). Atribut simplices dapat digunakan untuk menggantikan hasil library scipy.spatial ConvexHull, tetapi perlu diingat formatnya adalah List (bukan numpy array).

## Author
Bryan Amirul Husna / 13520146, Teknik Informatika ITB 2020