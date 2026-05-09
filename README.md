1. Dataset planets memiliki banyak missing value,
   terutama pada kolom mass dan distance.

2. Method penemuan planet tidak seimbang.
   Radial Velocity dan Transit adalah metode yang paling dominan.

3. orbital_period, mass, dan distance memiliki distribusi right-skewed.
   Mayoritas data berada pada nilai kecil,
   tetapi ada beberapa nilai ekstrem yang sangat besar.

4. Histogram biasa bisa terlihat menumpuk di kiri
   karena adanya nilai ekstrem di sisi kanan.
   Log scale membantu membuat distribusi lebih mudah dibaca.

5. Boxplot mass dan orbital_period menunjukkan banyak outlier di sisi kanan.
   Ini konsisten dengan histogram yang right-skewed.

6. Microlensing cenderung memiliki median distance yang lebih tinggi,
   sehingga metode ini terlihat berkaitan dengan penemuan planet yang lebih jauh.

7. Scatterplot mass vs orbital_period tidak menunjukkan hubungan linear yang kuat.
   Titik data menyebar luas dan terdapat outlier.

8. Scatterplot distance vs year menunjukkan bahwa penemuan planet
   semakin padat pada periode modern, terutama setelah tahun 2000-an.

9. Heatmap menunjukkan bahwa korelasi linear antar fitur numerik
   relatif lemah sampai sedang.
   Hubungan pada dataset ini tidak sesederhana hubungan linear biasa.

10. Dataset planets sangat cocok untuk belajar visualisasi karena memiliki:
    - missing value
    - distribusi skewed ekstrem
    - banyak outlier
    - kategori method
    - data tahun
    - kebutuhan log scale untuk membaca distribusi
