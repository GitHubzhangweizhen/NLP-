from keras.preprocessing.text import Tokenizer
samples = ['我 毕业 于 北京理工大学','我 就职 于 中国科学计算技术研究院']
#构建单词的索引
tokenizer = Tokenizer()
tokenizer.fit_on_texts(samples)
word_index = tokenizer.word_index
print(word_index)
print(len(word_index))
sequences = tokenizer.texts_to_sequences(samples)
print(sequences)
one_hot_result = tokenizer.texts_to_matrix(samples)
print(one_hot_result)
#123456 我 于 毕业 北京理工大学 就职 中国科学计算技术研究院
#优点：1 解决了分类器不好处理离散数据的问题
# 2 在一定程度上也起到了扩充特征的作用
# 缺点 1 它是一个词袋模型，不考虑词于词之间的顺序
# 2 它假设词于词之间是相互独立的（但是在大多数情况下，词与词之间是相互影响的） 3 它得到的特征是离散稀疏的