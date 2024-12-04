import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 设置图片目录和Excel文件路径
image_dir = r'E:\daore'
excel_file = r'E:\daore\shuju.xlsx'

# 读取Excel文件
df = pd.read_excel(excel_file)

# 确保列名与Excel中一致，这里假设Excel文件的列名分别是'图片名称', '热膨胀系数', '介电常数'
df.columns = ['image_name', 'CTE', 'dielectric_constant']

# 获取用户输入的筛选条件
try:
    dielectric_threshold = float(input("请输入介电常数的筛选值（例如：2.3）："))
    thermal_expansion_threshold = float(input("请输入热膨胀系数的筛选值（例如：60）："))
except ValueError:
    print("输入无效，请输入数字。")
    exit(1)

# 按照介电常数和热膨胀系数的条件进行筛选
filtered_df = df[(df['dielectric_constant'] < dielectric_threshold) & (df['CTE'] < thermal_expansion_threshold)]

# 随机选择 40 张符合条件的图片
filtered_images = filtered_df.sample(n=40, random_state=42)  # random_state 用于保证结果的可复现性

# 如果没有符合条件的图片，输出提示
if filtered_images.empty:
    print("没有符合筛选条件的图片。")
    exit(0)

# 显示符合条件的图片
fig, axes = plt.subplots(8, 5, figsize=(15, 24))  # 创建一个8x5的图像展示窗口（40张图片）
axes = axes.flatten()

for i, (index, row) in enumerate(filtered_images.iterrows()):
    image_name = row['image_name']
    image_path = os.path.join(image_dir, image_name)
    img = mpimg.imread(image_path)
    
    # 显示图片
    axes[i].imshow(img)
    axes[i].axis('off')  # 不显示坐标轴
    
    # 获取性能指标
    thermal_expansion = row['CTE']
    dielectric_constant = row['dielectric_constant']
    
    # 在图片下方添加性能指标的文字
    axes[i].set_title(f'{image_name}\nCTE: {thermal_expansion}\ndielectric_constant: {dielectric_constant}', fontsize=10, pad=10)

# 调整布局并展示图片
plt.tight_layout()
plt.show()
