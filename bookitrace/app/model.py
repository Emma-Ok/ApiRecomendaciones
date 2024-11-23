import pandas as pd
from surprise import Dataset, Reader, SVD

# Load data
ratings_data = pd.read_csv('data/ratings.csv.zip')
books_metadata = pd.read_csv('data/books.csv.zip')

# Prepare data for Surprise
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings_data[['user_id', 'book_id', 'rating']], reader)

# Train model
svd = SVD(verbose=True, n_epochs=10)
trainset = data.build_full_trainset()
svd.fit(trainset)

# Utility functions
from .utils import get_book_id, get_book_info, predict_review, generate_recommendation