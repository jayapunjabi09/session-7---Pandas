import pandas as pd

data = {
    'Item': ['Pizza', 'Burger', 'Pasta', 'Sandwich'],
    'Price': [200, 100, 150, 80],
    'Qty': [2, 3, 2, 4]
}

df = pd.DataFrame(data)

df['DiscountedPrice'] = df['Price'].apply(
    lambda x: x * 0.90
)

print("Food Items After 10% Discount:")
print(df)