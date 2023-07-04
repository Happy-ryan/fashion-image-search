# fashion-image-search
Input image, get back matching image fashion results, using Gradio and Fashion-CLIP

## Application Structure
![app-structure](/asset/structure.png)

## Dir Tree


```
fashion-image-search
├─ README.md
├─ asset
│  └─ structure.png
├─ back
│  ├─ embedding.py
│  ├─ search.py
│  ├─ proxy.py
│  ├─ infra
│  │  ├─ embedding
│  │  │  ├─ client.py
│  │  │  └─ model.py
│  │  ├─ metadata
│  │  └─ search
│  │     ├─ client.py
│  │     └─ model.py
│  ├─ models
│  │  ├─ __init__.py
│  │  └─ search.py
│  ├─ routes
│  │  ├─ __init__.py
│  │  ├─ embedding.py
│  │  ├─ proxy.py
│  │  └─ search.py
├─ front
│  ├─ flagged
│  └─ main.py
└─ jupyternotebook
│  ├─ httpx_test.ipynb
   └─ fashion-image-search-demo.ipynb
```