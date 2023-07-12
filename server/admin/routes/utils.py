import pandas as pd
from tqdm import tqdm

def makeJsonList(df: pd.DataFrame, type: str):
    jsonList = []
    for i in tqdm(range(len(df['key'].tolist()))):
        json_template = { "key": list(df['key'])[i],
                          "link": list(df['link'])[i],
                          "name": list(df['name'])[i],
                          "image_link": list(df['image_link'])[i],
                          "path": list(df['path'])[i],
                          "category": {
                              "type": type
                          }
                          }
        jsonList.append(json_template)
    return jsonList
        
            
