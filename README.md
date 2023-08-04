# fashion-image-search
Input image, get back matching image fashion results, using Gradio and Fashion-CLIP

## Application Structure
![app-structure](/asset/structure2.png)

## Dir Tree

```
fashion-image-search
├─ README.md
├─ asset
│  ├─ structure.png
│  └─ structure2.png
├─ front
│  └─ main.py
├─ requirments.txt
├─ server
│  ├─ admin
│  │  ├─ build.py
│  │  ├─ csv_editor.ipynb
│  │  ├─ infra
│  │  │  ├─ build
│  │  │  │  ├─ client.py
│  │  │  │  └─ model.py
│  │  │  └─ meta
│  │  │     └─ client.py
│  │  ├─ models
│  │  │  ├─ __init__.py
│  │  │  └─ build.py
│  │  ├─ proxy.py
│  │  └─ routes
│  │     ├─ __init__.py
│  │     ├─ build.py
│  │     └─ proxy.py
│  └─ customer
│     ├─ embedding.py
│     ├─ infra
│     │  ├─ embedding
│     │  │  ├─ client.py
│     │  │  └─ model.py
│     │  ├─ meta
│     │  │  └─ client.py
│     │  ├─ search
│     │  │  ├─ client.py
│     │  │  ├─ model.py
│     │  │  └─ utils.py
│     │  ├─ storage
│     │  │  └─ client.py
│     │  └─ translate
│     │     └─ client.py
│     ├─ models
│     │  ├─ __init__.py
│     │  ├─ embedding.py
│     │  └─ search.py
│     ├─ proxy.py
│     ├─ routes
│     │  ├─ __init__.py
│     │  ├─ embedding.py
│     │  ├─ proxy.py
│     │  └─ search.py
│     ├─ search.py
│     └─ storage