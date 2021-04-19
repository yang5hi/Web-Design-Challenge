'''
python program to change csv to html
the html table can be used in other html by
simply copy the <table>...</table>
'''
import pandas as pd
df=pd.read_csv("cities.csv")
df.to_html("cities_to_html.html",index=False)