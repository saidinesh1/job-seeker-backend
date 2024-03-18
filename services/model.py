import pandas as pd
from pre_processing import pre_process
df=pd.read_csv("jobs.csv")
df.insert(0, 'id', range(1, len(df) + 1))
df['combined_text']=df['title']+" "+df['description']

pre_processed_docs={}

for index, row in df.iterrows():
    preprocessed_text = pre_process(row['combined_text'])
    pre_processed_docs[row['id']] = preprocessed_text
