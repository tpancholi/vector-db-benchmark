from datetime import datetime

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer


def build_text_row(row):
	seeds = row.get("seeds", "")
	return f"{row['track']} by {row['artist']}. Genre: {row.get('genre', '')}. Tags: {seeds}"


def embed_data(
	df: pd.DataFrame, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
) -> np.ndarray:
	start_datetime = datetime.now()
	print(f"Starting to Embed data at {start_datetime}")
	model = SentenceTransformer(model_name)
	texts = df["text"].tolist()
	vectors = model.encode(
		texts, normalize_embeddings=True, show_progress_bar=True, convert_to_numpy=True
	)
	end_datetime = datetime.now()
	print(f"Completed Embedding data at {end_datetime}")
	ts = (end_datetime - start_datetime).total_seconds()
	m, s = divmod(ts, 60)
	print(f"Total time taken to Embed data: {int(m)} minutes {int(s)} seconds")
	return vectors
