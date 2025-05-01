import pandas as pd
#
# data = [1, 2, 3, 4, 5]
# s = pd.Series(data)
# print(s)
# data = {
#     "name": ["Ivan", "Petr", "Sergey"],
#     "age": [25, 30, 35],
#     "city": ["Moscow", "St. Petersburg", "Novosibirsk"]
# }
#
# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv("World-happiness-report-2024.csv")
# print(df[df['lowerwhisker' ] > 0.7])
# df = pd.read_csv("hh.csv")
# # df['Test'] = [ new for new in range(29)]
# # print(df)
#
# df.drop(28, axis=0, inplace=True)
#
# print(df)
df = pd.read_csv("animal.csv")
print(df)
#
# df.dropna(inplace=True)
# print(df)
group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)

dt.to_csv("new.csv", index=False) # сохранение
