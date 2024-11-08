from flask import Flask, url_for, render_template, request, flash
from markupsafe import Markup
import os
import json
app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/Nuclear")
def render_Nuclear():
    names = get_name_options()
    return render_template('Nuclear.html', name_options = names)
    
@app.route("/showFact")
def render_fact(): 
    names = get_name_options()
    Country = request.args.get('Country')
    yield1 = thing1(Country)
    yield2 = thing2(Country)
    avg = avg_yield(Country)
    test = "In " + (Country) + ", the lower yield is " + str(yield1) + " the higher yield is " + str(yield2) + ". The average KT of tnt is 12 and " + str(avg) + "."
    print(yield1)
    print(yield2)
    return render_template('Nuclear.html', name_options = names, t=test)
    
    
@app.route("/data")
def render_data():
    return render_template('data.html')

def get_name_options():
    with open('Nuclear.json') as nuclear_data:
        data = json.load(nuclear_data)
    names=[]
    for n in data:
        if n["Data"]["Name"] not in names:
            names.append(n["Data"]["Name"])
    options=""
    for n in names:
         options += Markup("<option value=\"" + str(n) + "\">" + str(n) + "</option>")
    return options
    
def thing1(Country):
    with open('Nuclear.json') as nuclear_data:
        data = json.load(nuclear_data)
    lowest=-1
    yield_option = ""
    for entry in data:
        if entry["Data"]["Name"] == Country:
            if entry["Data"]["Yield"]["Lower"] > lowest:
                yield_option = entry["Data"]["Yield"]["Lower"]
    return yield_option

def thing2(Country):
    with open('Nuclear.json') as nuclear_data:
        data = json.load(nuclear_data)
    highest=-1
    second_yield_option = ""
    for entry in data:
        if entry["Data"]["Name"] == Country:
            if entry["Data"]["Yield"]["Upper"] > highest:
                second_yield_option = entry["Data"]["Yield"]["Upper"]
    return second_yield_option
    
def avg_yield(Country):
    yield1 = thing1(Country)
    yield2 = thing2(Country)
    if yield1 is not None and yield2 is not None: #  <-perplexity this line
        return (yield2 + yield1) / 2
    else:
        return None
  
def total_sightings(years):
    years= {}
    for date in years:
        year = years["Date"]["Year"]
        if year not in years:
            years[year] = 1
        else:
            years[year] = years[year] + 1 
            
    years = dict(sorted(years.items()))
    code = "["
    for year, gross in years.items():
        code = code + Markup("{ x: '" + str(year) + "', y: " + str(gross) + " },")
    code = code[:-1]
    code = code + "]"
    print(code)
    return code

if __name__=="__main__":
    app.run(debug=True)
