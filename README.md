#       Bert-Pytorch-TextClassification

#  介绍
本文参考了一位大佬的代码，代码地址为：https://github.com/649453932/Bert-Chinese-Text-Classification-Pytorch
本文只用Bert模型进行中文文本分类的预实验

# 数据集
笔者自己搜集的论文数据集，读者可以去中国知网等论文网站自行搜集。
数据集放在Paper文件夹内
训练集|train.txt
验证集|dev.txt
测试集|test.txt
数据集格式：标签 + '\t' + 文本
class.txt内放入分类标签

# Bert中文预训练模型
bert的中文预训练模型放在 bert_pretain目录下，目录下为三个文件：
 - pytorch_model.bin  
 - bert_config.json  
 - vocab.txt  
 本文因为pytorch_model.bin文件太大上传不了，所以只提供了后两个文件，具体文件请看介绍中大佬提供的文件
 
 # BERT论文
 BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding  
 地址： https://arxiv.org/abs/1810.04805
