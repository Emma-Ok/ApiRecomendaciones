import difflib
import random

def get_book_id(book_title, metadata):
    existing_titles = list(metadata['title'].values)
    closest_titles = difflib.get_close_matches(book_title, existing_titles)
    book_id = metadata[metadata['title'] == closest_titles[0]]['id'].values[0]
    return book_id

def get_book_info(book_id, metadata):
    book_info = metadata[metadata['id'] == book_id][['id', 'isbn', 'authors', 'title', 'original_title']]
    return book_info.to_dict(orient='records')

def predict_review(user_id, book_title, model, metadata):
    book_id = get_book_id(book_title, metadata)
    review_prediction = model.predict(uid=user_id, iid=book_id)
    return review_prediction.est

def generate_recommendation(user_id, model, metadata, thresh=4, num_recommendations=4):
    book_titles = list(metadata['title'].values)
    random.shuffle(book_titles)
    
    recommendations = []
    for book_title in book_titles:
        rating = predict_review(user_id, book_title, model, metadata)
        if rating >= thresh:
            book_id = get_book_id(book_title, metadata)
            recommendations.append(get_book_info(book_id, metadata))
            if len(recommendations) == num_recommendations:
                break
    return recommendations