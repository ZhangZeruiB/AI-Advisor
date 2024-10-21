import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

investor = pd.read_csv(r'E:\Github\AI-Advisor\data\NFCS 2021 Investor Data 221121.csv')
state = pd.read_csv(r'E:\Github\AI-Advisor\data\NFCS 2021 State Data 220627.csv')

investor_clean = investor[(investor != 98).all(axis=1) & (investor != 99).all(axis=1)]
state_clean = state[(state != 98).all(axis=1) & (state != 99).all(axis=1)]
merged_df = pd.merge(investor_clean, state_clean, on='NFCSID', how='left')
merged_df.to_csv(r'E:\Github\AI-Advisor\data\merged_df.csv', index=False)