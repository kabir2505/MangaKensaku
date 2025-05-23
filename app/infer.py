import faiss
import numpy as np
from PIL import Image
from sentence_transformers import SentenceTransformer
import matplotlib.pyplot as plt
import os
import json
import requests
import urllib.request
from PIL import Image
from io import BytesIO
import urllib.request
import urllib
from functools import partial



class FaissSearch():
    def __init__(self,index_path:str,cloudinary_map_path:str):
        self.index_path=index_path
        self.cloudinary_map_path=cloudinary_map_path
        
        self.model=SentenceTransformer('clip-ViT-B-32')
        self.index,self.image_urls=self._load_faiss_index()
    
    def _load_faiss_index(self):
        index=faiss.read_index(self.index_path)
        with open(self.index_path+'.paths','r') as f:
            local_image_names=[os.path.basename(line.strip()) for line in f]
        
        with open(self.cloudinary_map_path,"r") as f:
            cloudinary_map=json.load(f)
        
        image_urls=[]
        missing=0
        
        for name in local_image_names:
            url=cloudinary_map.get(name)
            if url:
                image_urls.append(url)
            else:
                missing+=1
                image_urls.append(cloudinary_map.get("image336.jpg")) #placeholder for missing images
        
        print(f"Index loaded with {len(image_urls)} entries, {missing} missing from Cloudinary map")
        
        return index, image_urls



    def retrieve_similar_images(self,query:str,top_k:int=10):
        query_features=self.model.encode(query)
        query_features=query_features/np.linalg.norm(query_features)
        query_features = query_features.astype(np.float32).reshape(1, -1)
        
        distances,indices=self.index.search(query_features,top_k)
        
        similar_images=[self.image_urls[i] for i in indices[0]]
        
        return similar_images
            
    
        
faiss_search_engine = FaissSearch("faiss/faiss_index", "faiss/cloudinary_map.json")
