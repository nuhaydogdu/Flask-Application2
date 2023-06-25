from flask import Flask, render_template
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from publications import MyPublications
from bs4 import BeautifulSoup
app = Flask(__name__)
import json
from collections import Counter

def parse_data_to_dataframe(data):
    df = pd.DataFrame(data)
    return df
    
def convert_data_to_json(input_array):
    result = []
    for item in input_array:
        content = item.text.strip('span')
        values = content.split(',')
        
        obj = {'title': values[0].strip(), 'page': values[1].strip(), 'year': values[2].strip().rstrip('.')}

        result.append(obj)

    with open('data.json', 'w') as json_file:
        json.dump(result, json_file)

@app.route("/")
def main():
    publications = MyPublications()   
    articles = publications.update_my_list()
    convert_data_to_json(articles["second_span"])
    
    new_author_array = []
    for item in articles["author_span"]:
        tag_text = item.text
        names = tag_text.split(", ")
        for name in names:
            if name.strip() != "B Canbula":
                new_author_array.append(name.strip())
    
    print(new_author_array)
    
    author_counts = Counter(new_author_array)
    author_list = list(author_counts.keys())
    count_list = list(author_counts.values())

    with open("data.json") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    
    df_data = parse_data_to_dataframe(json_data)
    
    return render_template("index.html",
                           titles=df_data["title"].tolist(),
                           pages=df_data["page"].tolist(),
                           years=df_data["year"].tolist(),
                           content=df_data.to_html(),
                           authors=author_list,
                           numbers=count_list
                           )
                        
if __name__ == "__main__":
    app.run()
