from fastapi import APIRouter, HTTPException
from .model import svd, books_metadata, generate_recommendation

router = APIRouter()

@router.get('/recommend')
def recommend(user_id: int, num_recommendations: int = 4):
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    
    recommendations = generate_recommendation(user_id, svd, books_metadata, num_recommendations=num_recommendations)
    if recommendations:
        return recommendations
    else:
        raise HTTPException(status_code=404, detail="No recommendations found")