import httpx

# --search server에 search 요청
class SearchClient:
    ## -- search server api url
    API_URL = "http://localhost:9001/search"
    print("여기 밑으로 못 내려가는건가?")
    async def search(self, embedding: list[float]) -> (list[float], list[int]):
        async with httpx.AsyncClient() as client:
            print("여기는 들어왔나?")
            response = await client.post(
                f"{self.API_URL}",
                json={
                    "embedding": embedding
                    },
                timeout=None
            )
        
            print("response의 Status_code는 여기에 있다!", response.status_code)
            
            dists = response.json()["dists"]
            ids = response.json()["ids"]
        
        return dists, ids