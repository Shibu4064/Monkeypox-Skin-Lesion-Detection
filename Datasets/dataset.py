import kagglehub

# https://www.kaggle.com/datasets/joydippaul/mpox-skin-lesion-dataset-version-20-msld-v20(Multiclass)

# Download latest version
path1 = kagglehub.dataset_download("joydippaul/mpox-skin-lesion-dataset-version-20-msld-v20")

# https://www.kaggle.com/datasets/nafin59/monkeypox-skin-lesion-dataset
# Download latest version
path2 = kagglehub.dataset_download("nafin59/monkeypox-skin-lesion-dataset")


print("Path to dataset files:", path1)
print("Path to dataset files:", path2)
