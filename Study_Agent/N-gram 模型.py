
# import collections
# # 目标：使用 Bigram (N=2) 模型，估算句子 datawhale agent learns 出现的概率
# #语料库
# corpus = "datawhale agent learns datawhale agent works"
# tokens = corpus.split()
# total_token = len(tokens)

# #一、计算P(datawhale)
# count_datawhale=tokens.count('datawhale')
# p_datawhale=count_datawhale/total_token
# print(f'P(datawhale)={p_datawhale:.3f}')

# # 二、计算P(agent|datawhale)
# bigrams=zip(tokens,tokens[1:])
# bigrams_counts=collections.Counter(bigrams)
# count_datawhale_agent=bigrams_counts[('datawhale','agent')]
# p_datawhale_agent=count_datawhale_agent/count_datawhale
# print(f'P(agent|datawhale)={p_datawhale_agent:.3f}')

# #三、计算P(learns|agent)
# count_agent_learns=bigrams_counts[('agent','learns')]
# count_agent=tokens.count('agent')
# p_agent_learns=count_agent_learns/count_agent
# print(f'P(learns|agent)={p_agent_learns:.3f}')

# #四、将概率连乘
# p_sentence=p_datawhale*p_datawhale_agent*p_agent_learns
# print(f'P(datawhale agent learns)={p_sentence:.3f}')


import collections
# 目标：使用 Bigram (N=2) 模型，估算句子 agent works 出现的概率
#语料库
corpus = "datawhale agent learns datawhale agent works"
tokens = corpus.split()
total_token = len(tokens)

#一、计算P(agent)
count_agent=tokens.count('agent')
p_agent=count_agent/total_token
print(f'P(agent)={p_agent:.3f}')

# 二、计算P(works|agent)
bigrams=zip(tokens,tokens[1:])
bigrams_counts=collections.Counter(bigrams)
count_agent_works=bigrams_counts[('agent','works')]
p_agent_works=count_agent_works/count_agent
print(f'P(works|agent)={p_agent_works:.3f}')



#四、将概率连乘
p_sentence=p_agent*p_agent_works
print(f'P(agent works)={p_sentence:.3f}')