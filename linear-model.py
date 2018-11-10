import pandas as pd
from sklearn.linear_model import LinearRegression
bmi_life_data = pd.read_csv("bmi_and_life_expectancy.csv")
bmi_life_model = LinearRegression()
