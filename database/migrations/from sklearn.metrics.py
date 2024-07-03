from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

cosine_similarities = cosine_similarity(tfidf_matrix)
cosine_similarities_df = pd.DataFrame(cosine_similarities, index=range(1, len(berita_hoax) + 1), columns=range(1, len(berita_hoax) + 1))

print(cosine_similarities_df)
