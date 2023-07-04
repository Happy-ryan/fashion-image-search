import httpx

# --embedding server에 embedding 요청
class EmbeddingClient:
    # --embedding server api
    API_URL = "http://localhost:9000/embedding"
    
    async def get_image_embedding(self, rid):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.API_URL}/image/{rid}",
                timeout=None
            )
            
            embedding = response.json()["embedding"]
            return embedding
        
    
    async def get_text_embedding(self, text: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.API_URL}/text",
                timeout=None,
                json = {
                    "text": text,
                }
            )
            
            embedding = response.json()["embedding"]
            return embedding            