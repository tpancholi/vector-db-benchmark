<<<<<<< HEAD
import argparse
from pathlib import Path

=======
>>>>>>> 5a3e66d (initial embedding code)
import numpy as np
import pandas as pd
from datetime import datetime

from sentence_transformers import SentenceTransformer

<<<<<<< HEAD
from utils.config import settings

=======
>>>>>>> 5a3e66d (initial embedding code)

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
<<<<<<< HEAD


def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("--csv", required=True, help="Path to CSV file")
	ap.add_argument("--out", required=True, help="Path to output file")
	ap.add_argument("--model", default=None, help="Huggingface Embedding Model name")
	args = ap.parse_args()

	df = pd.read_csv(args.csv)
	df["text"] = df.apply(build_text_row, axis=1)

	embedding_model_name = args.model or settings.EMBEDDING_MODEL
	vectors = embed_data(df, model_name=embedding_model_name)

	out_path = Path(args.out)
	out_path.parent.mkdir(parents=True, exist_ok=True)

	df_out = df.copy()
	df_out["embedding"] = list(map(lambda v: v.tolist(), vectors))
	df_out.to_parquet(out_path, index=False)
	print(f"Saved {len(df_out)} embedded rows to {out_path}")


if __name__ == "__main__":
	main()
=======
>>>>>>> 5a3e66d (initial embedding code)
