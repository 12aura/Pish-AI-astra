import numpy as np # type: ignore
import pandas as pd # type: ignore

df = pd.read_csv('spam.csv')

df.sample(5)
