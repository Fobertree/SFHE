import bz2
import os
from tqdm import tqdm

path = ""

with bz2.open(os.path.join("Data", path)) as bz_file:
    for line in tqdm(bz_file):
        label, text = line.rstrip("\n").split("\t")
        text_words = text.split(", ")
        print(label)

dataset_path = os.path.join("Data", "data")

train_dir = os.path.join(os.path.join("Data", "train"))
