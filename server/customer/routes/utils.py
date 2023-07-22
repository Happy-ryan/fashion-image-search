from collections import defaultdict
import googletrans


def objectIdDecoder(list):
  results=[]
  for doc in list:
    dic = defaultdict()
    columns = ['key', 'brand', 'category', 'check','image_link', 'link', 'meta', 'name', 'price', 'subcategory']
    for col in columns:
      # if doc[col] == 'nan':
      #   print("nan이 있다!", doc['key'])
      #   continue
      dic[col] = doc[col]
    # dic['key'] = doc['key']
    # dic['brand'] = doc['brand']
    # dic['category'] = doc['category']
    # dic['check'] = doc['check']
    # dic['image_link'] = doc['image_link']
    # dic['link'] = doc['link']
    # dic['meta'] = doc['meta']
    # dic['name'] = doc['name']
    # dic['price'] = doc['price']
    # dic['subcategory'] = doc['subcategory']
    results.append(dic)
  return results


def translate_text(text: str):
    translator = googletrans.Translator()
    result = translator.translate(text, dest='en')
    return result.text