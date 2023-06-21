import faiss
import os
import numpy as np
import pickle

'''
faiss 사용법 참고 : 2단계에 걸쳐서 진행, 변수는 웬만해서는 np.array로 들어간다.
1) output_embeddings에 id 부여 (현재는 output_embeddigs를 pkl로 저장함)
index.add_with_ids(output_embs, ids) -> 각 임베딩과 id를 매칭시켜주는 작업
2) 입력으로 들어온 input_embedding과 유사도 검색
result = index.search(input_emb.reshape(1, -1), 2) <- input_emb: np.array
(array([[94.22209, 89.08495]], dtype=float32), array([[32, 34]]))
'''

class SearchModel:
    DATA_PATH = 'storage/embedding'
    
    
    def __init__(self):
        index = faiss.IndexFlatIP(512) #--embedding의 차원 수,
        self.index = faiss.IndexIDMap2(index) # --embedding에 id를 부여하기위해서
    
        ids = []
        embs = []
        for filename in os.listdir(self.DATA_PATH):
            id = filename.split(".")[0] # 000.pkl
            ids.append(id)
            with open(os.path.join(self.DATA_PATH, filename), "rb") as f:
                emb = pickle.load(f)
                embs.append(emb)
        self.index.add_with_ids(np.array(embs), np.array(ids))
        
        
    def search(self, embedding: list[float]) -> (list[float], list[int]):
        dists, ids = self.index.search(np.array(embedding).reshape(1, -1), 2)
        print("dists.dtype은 여기에 있다!", dists.dtype)
        return dists.flatten().tolist(), ids.flatten().tolist()
        
        
        
        