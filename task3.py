import pandas as pd

data = {
    'PostID': [101, 102, 103, 104],
    'Likes': [1500, 2500000, 50000, 1200000],
    'Comments': [200, 15000, 3000, 10000]
}

df = pd.DataFrame(data)

def format_number(num):
    if num >= 1000000:
        return str(round(num / 1000000, 1)) + 'M'
    elif num >= 1000:
        return str(round(num / 1000, 1)) + 'K'
    else:
        return str(num)

df['Likes'] = df['Likes'].apply(format_number)
df['Comments'] = df['Comments'].apply(format_number)

print("Instagram Data:")
print(df)