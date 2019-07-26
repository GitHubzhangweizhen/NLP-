import numpy as np
samples = ['我 毕业 于 北京理工大学','我 就职 于 中国科学院技算技术研究所']
#为文本做一个索引，或者说是编号
token_index = {}
for sample in samples:
    for word in sample.split():
        if word not in token_index:
            token_index[word] = len(token_index) + 1
print(len(token_index))
print(token_index)
results1 = np.zeros(shape=(len(samples),len(token_index) + 1,max(token_index.values())+1))
results1.shape
for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split())):
        index = token_index.get(word)
        print(j,index,word)
        results1[i,j,index] = 1   #编码
results1
results2 = np.zeros(shape=(len(samples),max(token_index.values()) + 1))
for i, sample in enumerate(samples):
    for _,word in list(enumerate(sample.split())):
        print(word)
        index = token_index.get(word)
        print(index)
        results2[i,index] = 1
results2