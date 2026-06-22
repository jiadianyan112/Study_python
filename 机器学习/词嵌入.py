
import numpy as np

#二维词向量
embeddings= {
    "king":np.array([0.9,0.8]),
    "queen":np.array([0.9,0.2]),
    "man":np.array([0.7,0.9]),
    "woman":np.array([0.7,0.3])
}

#计算余弦相似度
def  cosine_similarity(vec1,vec2):
    dot_product = np.dot(vec1,vec2)
    norm_product = np.linalg.norm(vec1)*np.linalg.norm(vec2)
    return dot_product/norm_product

#king-man+women
result_vec=embeddings["king"]-embeddings["man"]+embeddings["woman"]

sim =cosine_similarity(result_vec,embeddings["queen"])

print(f"king - man + woman 的结果向量: {result_vec}")
print(f"该结果与 'queen' 的相似度: {sim:.4f}")