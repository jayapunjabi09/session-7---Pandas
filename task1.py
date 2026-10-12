import pandas as pd

data = {
    'ProductName': ['Pizza', 'Burger', 'Pasta', 'Sandwich'],
    'Price': [200, 100, 150, 80],
    'Qty': [2, 3, 2, 4]
}

df = pd.DataFrame(data)

df['TotalValue'] = df['Price'] * df['Qty']

print("Updated Product Data:")
print(df)