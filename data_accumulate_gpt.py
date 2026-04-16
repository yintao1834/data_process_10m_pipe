from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
CASE_DIR = BASE_DIR / "data" / "case1"

# 生成文件路径
data_paths = [
    CASE_DIR / f"{num}({2.5 * num}-{2.5 * num})_strain.csv"
    for num in range(1, 13)
]

result_df = pd.DataFrame()
cumulative = None
reference_distance = None

for i, path in enumerate(data_paths, start=1):
    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {path}")

    df = pd.read_csv(path,
        encoding="cp932",
        usecols=["Distance (m)", "Time 1"]
    )

    # 第一次读取时，记录标准距离轴
    if reference_distance is None:
        # 一定养成copy的习惯，这样后面对 df 修改，不会影响 reference_distance
        reference_distance = df["Distance (m)"].copy()  
        result_df.index = reference_distance
        result_df.index.name = "Distance (m)"
    else:
        # 检查后续文件的距离轴是否一致
        if not df["Distance (m)"].equals(reference_distance):
            raise ValueError(f"距离轴不一致，文件有问题: {path}")

    current_strain = df["Time 1"].copy()

    if cumulative is None:
        cumulative = current_strain
    else:
        cumulative = cumulative + current_strain

    column_name = f"{2.5 * i}mm"
    result_df[column_name] = cumulative.to_numpy()

print(result_df.head())

# 如需导出：
# output_path = BASE_DIR / "case1_cumulative_strain.csv"
# result_df.to_csv(output_path, encoding="utf-8-sig")