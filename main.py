import pandas as pd

# 1️⃣ 创建一个 DataFrame（类似表格）
data = {
    "姓名": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "年龄": [25, 30, 35, 40, 28],
    "城市": ["北京", "上海", "广州", "深圳", "杭州"],
    "工资": [5000, 6000, 7000, 8000, 5500]
}

df = pd.DataFrame(data)

print("原始数据：")
print(df)

# 2️⃣ 查看数据基本信息
print("\n数据基本信息：")
print(df.info())

print("\n数据统计描述：")
print(df.describe())

# 3️⃣ 筛选数据
# 筛选年龄大于30的人
older_than_30 = df[df["年龄"] > 30]
print("\n年龄大于30的人：")
print(older_than_30)

# 4️⃣ 增加新列
df["工资增长"] = df["工资"] * 1.1  # 假设每个人涨 10%
print("\n增加工资增长列：")
print(df)

# 5️⃣ 分组聚合
# 按城市统计平均工资
avg_salary_by_city = df.groupby("城市")["工资"].mean()
print("\n按城市统计平均工资：")
print(avg_salary_by_city)

# 6️⃣ 排序
df_sorted = df.sort_values(by="年龄", ascending=False)
print("\n按年龄降序排序：")
print(df_sorted)

# 7️⃣ 保存到 CSV
df.to_csv("员工数据.csv", index=False)