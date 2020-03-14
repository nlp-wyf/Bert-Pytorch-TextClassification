from tqdm import tqdm

# 测试data文件夹中数据集的格式
path = 'E:/MyPrograms/Bert-Chinese-Text-Classification-Pytorch-master/Papers/data/test.txt'
with open(path, 'r', encoding='UTF-8') as f:
    for line in tqdm(f):
        lin = line.strip()
        if not lin:
            continue
        label, content = lin.split('\t')
        print(label + '\t' + content)
