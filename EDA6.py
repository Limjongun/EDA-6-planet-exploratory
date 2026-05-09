# ============================================================
# VISUAL EDA IRIS DATASET
# Fokus: Memahami Histogram, Boxplot, Scatterplot, Pairplot
# ============================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = sns.load_dataset('iris')

print("Head dataset:")
print(df.head())

print("\nTail dataset:")
print(df.tail())

print("\nShape dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInfo dataset:")
print(df.info())

print("\nStatistik deskriptif:")
print(df.describe())

print("\nMissing value:")
print(df.isnull().sum())


# ============================================================
# 2. COUNTPLOT SPECIES
# ============================================================

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='species')
plt.title("Jumlah Data Berdasarkan Species")
plt.xlabel("Species")
plt.ylabel("Jumlah")
plt.show()


# ============================================================
# 3. HISTOGRAM SEPAL LENGTH
# ============================================================

plt.figure(figsize=(7, 4))
sns.histplot(data=df, x='sepal_length', kde=True)
plt.title("Distribusi Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()


# ============================================================
# 4. HISTOGRAM PETAL LENGTH BERDASARKAN SPECIES
# ============================================================

plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x='petal_length',
    hue='species',
    kde=True
)

plt.title("Distribusi Petal Length Berdasarkan Species")
plt.xlabel("Petal Length")
plt.ylabel("Frequency")
plt.show()


# ============================================================
# 5. BOXPLOT PETAL LENGTH BERDASARKAN SPECIES
# ============================================================

plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x='species', y='petal_length')
plt.title("Petal Length Berdasarkan Species")
plt.xlabel("Species")
plt.ylabel("Petal Length")
plt.show()


# ============================================================
# 6. BOXPLOT SEMUA FITUR BERDASARKAN SPECIES
# ============================================================

numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

for column in numeric_columns:
    plt.figure(figsize=(7, 5))
    sns.boxplot(data=df, x='species', y=column)
    plt.title(f"{column} Berdasarkan Species")
    plt.xlabel("Species")
    plt.ylabel(column)
    plt.show()


# ============================================================
# 7. SCATTERPLOT PETAL LENGTH VS PETAL WIDTH
# ============================================================

plt.figure(figsize=(7, 5))
sns.scatterplot(
    data=df,
    x='petal_length',
    y='petal_width',
    hue='species'
)

plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()


# ============================================================
# 8. SCATTERPLOT SEPAL LENGTH VS SEPAL WIDTH
# ============================================================

plt.figure(figsize=(7, 5))
sns.scatterplot(
    data=df,
    x='sepal_length',
    y='sepal_width',
    hue='species'
)

plt.title("Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()


# ============================================================
# 9. PAIRPLOT IRIS
# ============================================================

sns.pairplot(df, hue='species')
plt.show()


# ============================================================
# 10. CORRELATION HEATMAP
# ============================================================

numeric_df = df.select_dtypes(include=['int64', 'float64'])

correlation = numeric_df.corr()

print("\nCorrelation matrix:")
print(correlation)

plt.figure(figsize=(8, 5))
sns.heatmap(correlation, annot=True, fmt=".2f")
plt.title("Correlation Heatmap Iris Dataset")
plt.show()


# ============================================================
# 11. FINAL INSIGHT
# ============================================================

print("""
FINAL INSIGHT VISUAL EDA IRIS:

1. Dataset iris memiliki 150 baris dan 5 kolom.
   Dataset ini terdiri dari 4 fitur numerik dan 1 fitur kategorikal species.

2. Jumlah data tiap species seimbang.
   Setosa, versicolor, dan virginica masing-masing memiliki jumlah data yang sama.

3. Histogram membantu melihat distribusi fitur numerik.
   Distribusi umum kadang terlihat seperti gabungan beberapa kelompok
   karena data berasal dari tiga species berbeda.

4. Boxplot menunjukkan bahwa petal_length dan petal_width
   sangat berbeda antar species.

5. Setosa memiliki petal_length dan petal_width paling kecil.
   Virginica cenderung memiliki petal_length dan petal_width paling besar.
   Versicolor berada di tengah.

6. Scatterplot petal_length vs petal_width menunjukkan hubungan positif.
   Semakin panjang petal, petal_width juga cenderung meningkat.

7. Scatterplot juga menunjukkan cluster species yang cukup jelas.
   Setosa paling mudah dipisahkan dari dua species lain.

8. Sepal_length dan sepal_width tidak memisahkan species sejelas fitur petal.
   Artinya, fitur petal lebih informatif untuk membedakan species.

9. Pairplot memperkuat bahwa petal_length dan petal_width
   adalah fitur paling kuat untuk membedakan species.

10. Heatmap menunjukkan korelasi positif kuat antara petal_length dan petal_width.
""")