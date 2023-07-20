from collections import defaultdict

def objectIdDecoder(list):
  results=[]
  for doc in list:
    dic = defaultdict()
    dic['key'] = doc['key']
    dic['link'] = doc['link']
    dic['name'] = doc['name']
    dic['image_link'] = doc['image_link']
    dic['category'] = doc['category']
    results.append(dic)
  return results
