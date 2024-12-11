from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.services.data_service import DataService
from app.models.data_models import DataRequest, DataResponse

router = APIRouter()
data_service = DataService()

@router.post("/process", response_model=DataResponse)
async def process_data(request: DataRequest, background_tasks: BackgroundTasks):
    try:
        result = await data_service.process_data(request.data)
        
        background_tasks.add_task(data_service.background_processing, result)
        
        return DataResponse(
            status="success",
            message="Dados processados com sucesso",
            result=result
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 