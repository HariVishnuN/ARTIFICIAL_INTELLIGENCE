import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
ratings_dict = {
    'User': ['User_A', 'User_B', 'User_C', 'User_D'],
    'Movie_1': [5, 4, 1, np.nan],
    'Movie_2': [4, np.nan, 1, 5],
    'Movie_3': [3, 5, np.nan, 2],   # Fixed: Added ratings list for Movie_3
    'Movie_4': [np.nan, 2, 4, 4]
}
df = pd.DataFrame(ratings_dict).set_index('User')
df_filled = df.apply(lambda row: row.fillna(row.mean()), axis=1)
item_similarity = cosine_similarity(df_filled.T)
item_sim_df = pd.DataFrame(item_similarity, index=df.columns, columns=df.columns)
print("Item Similarity Matrix:\n", item_sim_df)
print("\nRecommendation Baseline Complete.")