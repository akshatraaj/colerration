import plotly.express as px
import csv

with open(r"E:\rv\whitehatjr\python\colleration\data\Ice-Cream_vs_Cold-Drink_vs_Temperature_Ice_Cream_Sale_vs_Temperature_data.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Temperature", y="Ice-cream Sales(rupees)")
    fig.show()
