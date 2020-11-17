import glasscrap as gs 
import pandas as pd

path = '/home/user-one/DataScienceProject/ds_salary_proj/chromedriver_linux64/chromedriver'


df = gs.get_jobs("data scientist", 15, False, path, 15)

print(df)


