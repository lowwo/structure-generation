import numpy as np
from PIL import Image
import random
import math

def generate_hollow_spheres(
    image_width=500,
    image_height=500,
    sphere_radius=30,
    shell_thickness=8,
    max_spheres=50,
    max_attempts=100
):
    """
    生成随机分布的空心球二维结构图像。
    
    参数:
    - image_width: 图像宽度
    - image_height: 图像高度
    - sphere_radius: 空心球半径
    - shell_thickness: 球壳厚度
    - max_spheres: 最大空心球数量
    - max_attempts: 放置空心球的最大尝试次数
    
    返回:
    - PIL图像对象
    """
    
    # 初始化图像为黑色背景
    image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    
    # 存储已放置的球的中心坐标
    centers = []
    
    attempts = 0
    while len(centers) < max_spheres and attempts < max_attempts:
        attempts += 1
        # 随机选择一个中心位置，确保整个球在图像范围内
        x = random.randint(sphere_radius, image_width - sphere_radius)
        y = random.randint(sphere_radius, image_height - sphere_radius)
        
        # 检查是否与已有的球重叠
        overlap = False
        for (cx, cy) in centers:
            distance = math.hypot(cx - x, cy - y)
            if distance < 2 * sphere_radius + shell_thickness:
                overlap = True
                break
        if not overlap:
            centers.append((x, y))
    
    print(f"放置了 {len(centers)} 个空心球，尝试次数：{attempts}")
    
    # 为每个球绘制球壳和内部
    for (cx, cy) in centers:
        for i in range(image_height):
            for j in range(image_width):
                dist = math.hypot(cx - j, cy - i)
                if sphere_radius - shell_thickness <= dist <= sphere_radius:
                    image[i, j] = [128, 128, 128]  # 灰色球壳
                elif dist < sphere_radius - shell_thickness:
                    image[i, j] = [255, 255, 255]  # 白色内部
    
    # 转换为PIL图像
    pil_image = Image.fromarray(image)
    return pil_image

if __name__ == "__main__":
    # 生成图像
    img = generate_hollow_spheres(
        image_width=500,
        image_height=500,
        sphere_radius=30,
        shell_thickness=10,
        max_spheres
