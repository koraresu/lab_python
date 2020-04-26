import pandas as pd

def order_dataframe():
	dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
	       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
	       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
	       "population": [200.4, 143.5, 1252, 1357, 52.98] }

	dict_dataframe = pd.DataFrame(dict)
	print(dict_dataframe.sort_values(by=['country']))