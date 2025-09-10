import argparse
from pathlib import Path

import pandas as pd

from embeddings.embed import build_text_row, embed_data
from utils.config import settings


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
