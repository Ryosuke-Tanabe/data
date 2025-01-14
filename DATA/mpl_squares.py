import matplotlib.pyplot as plt

plt.style.available

# 利用可能なスタイルをリスト表示
# print(plt.style.available)

input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [1, 4, 9, 16, 25, 36, 47, 64, 81, 100]

plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)
ax.plot(input_values, squares, linewidth=3)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 目盛ラベルのサイズを設定する
ax.tick_params(axis="both", labelsize=14)

plt.show()
