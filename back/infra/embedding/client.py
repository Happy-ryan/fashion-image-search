import httpx

# --embedding server에 embedding 요청
class EmbeddingClient:
    # --embedding server api
    API_URL = "http://localhost:9000/embedding"
    
    async def get_embedding(self, rid):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.API_URL}/{rid}",
            )
            
            embedding = response.json()["embedding"]
            return embedding