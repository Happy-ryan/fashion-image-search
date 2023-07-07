# fashion-image-search
Input image, get back matching image fashion results, using Gradio and Fashion-CLIP

## Application Structure
![app-structure](/asset/structure2.png)

## Dir Tree


```
fashion-image-search
├─ README.md
├─ asset
│  └─ structure2.png
├─ back
│  ├─ embedding.py
│  ├─ infra
│  │  ├─ embedding
│  │  │  ├─ client.py
│  │  │  └─ model.py
│  │  ├─ metadata
│  │  └─ search
│  │     ├─ client.py
│  │     ├─ model.py
│  │     └─ utils.py
│  ├─ models
│  │  ├─ __init__.py
│  │  ├─ embedding.py
│  │  ├─ proxy.py
│  │  └─ search.py
│  ├─ proxy.py
│  ├─ routes
│  │  ├─ __init__.py
│  │  ├─ embedding.py
│  │  ├─ proxy.py
│  │  └─ search.py
│  └─ search.py
├─ front
│  └─ main.py
├─ jupyternotebook
│  └─ fashion-image-search-demo.ipynb
│  ├─ httpx_test.ipynb
│  └─ iter_test.ipynb
└─ requirments.txt
```