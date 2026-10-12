import pandas as pd

data = {
    'Product': ['Jeans', 'Tshirt', 'Shoes', 'Dress'],
    'Price': [1200, 500, 2000, 1500],
    'Qty': [2, 3, 1, 2]
}

df = pd.DataFrame(data)

def calculate_gst(row):
    return row['Price'] * row['Qty'] * 0.05

df['GST'] = df.apply(calculate_gst, axis=1)

print("Myntra Orders with GST:")
print(df)