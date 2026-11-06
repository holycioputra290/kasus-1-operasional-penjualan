import numpy as np
import pandas as pd

np.random.seed(42)

produk_list = [
    ('Laptop', 'Elektronik', 8500000, 2000000),
    ('Smartphone', 'Elektronik', 4500000, 1000000),
    ('Mouse', 'Elektronik', 150000, 30000),
    ('Buku', 'Pendidikan', 75000, 15000),
    ('Modul Ajar', 'Pendidikan', 120000, 25000),
    ('Kamus', 'Pendidikan', 180000, 35000),
]

n_rows = 1000
start_date = pd.to_datetime('2024-01-01')
end_date = pd.to_datetime('2024-12-31')

dates = start_date + pd.to_timedelta(
    np.random.randint(0, (end_date - start_date).days, n_rows), unit='D'
)
selected_indices = np.random.choice(len(produk_list), size=n_rows)

produk_col = [produk_list[i][0] for i in selected_indices]
kategori_col = [produk_list[i][1] for i in selected_indices]

harga_col = [
    max(
        10000,
        int(
            np.random.normal(produk_list[i][2], produk_list[i][3]) // 1000 * 1000
        ),
    )
    for i in selected_indices
]

jumlah_col = []
for i in selected_indices:
    if produk_list[i][1] == 'Elektronik':
        jumlah_col.append(int(np.random.poisson(lam=15) + 1))
    else:
        jumlah_col.append(int(np.random.poisson(lam=60) + 1))

df = pd.DataFrame({
    'Tanggal': dates,
    'Produk': produk_col,
    'Kategori': kategori_col,
    'Harga (Rp)': harga_col,
    'Jumlah Terjual': jumlah_col,
})

df['Total Penjualan (Rp)'] = df['Harga (Rp)'] * df['Jumlah Terjual']
df = df.sort_values('Tanggal').reset_index(drop=True)

df.to_csv('dataset_operasional_penjualan.csv', index=False)
print('✅ File dataset_operasional_penjualan.csv berhasil dibuat!')