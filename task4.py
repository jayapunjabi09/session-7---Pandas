import pandas as pd

data = {
    'Restaurant': ['Pizza Hut', 'Dominos', 'KFC', 'Subway'],
    'Price': [250, 200, 300, 150],
    'Qty': [2, 3, 1, 4],
    'DeliveryCharge': [40, 30, 50, 20]
}

df = pd.DataFrame(data)

df['FinalAmount'] = df.apply(
    lambda row: row['Price'] * row['Qty']
    + row['DeliveryCharge'],
    axis=1
)

print("Zomato Orders:")
print(df)