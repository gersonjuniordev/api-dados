import pandas as pd
from typing import List, Any

class DataService:
    async def process_data(self, data: List[Any]) -> dict:
        """
        Processa os dados recebidos de forma assíncrona
        """
        df = pd.DataFrame(data)
        
        result = {
            "total_rows": len(df),
            "summary": df.describe().to_dict()
        }
        
        return result
    
    async def background_processing(self, data: dict):
        """
        Realiza processamento adicional em background
        """
        pass 