from flask import Flask, render_template, json,Response, jsonify, request, redirect
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    test = [
    [
      "Tiger Nixon",
      "System Architect",
      "Edinburgh",
      "5421",
      "2011/04/25",
      "$320,800"
    ],
    [
      "Garrett Winters",
      "Accountant",
      "Tokyo",
      "8422",
      "2011/07/25",
      "$170,750"
    ]]

    df = pd.read_csv('static/data/2ndiat.csv')[['analyst','create_dt','iat_id','iat_name','summary_offices']]
    csv = df.to_json(orient='records')

    secdf = pd.read_csv('static/data/iat.csv')[['analyst','create_dt','iat_id','iat_name','summary_offices']]
    seccsv = secdf.to_json(orient='records')


    return render_template("test.html",test=test,csv=csv, seccsv=seccsv)


# def secindex():
#     sectest = [
#     [
#       "Tiger Nixon",
#       "System Architect",
#       "Edinburgh",
#       "5421",
#       "2011/04/25",
#       "$320,800"
#     ],
#     [
#       "Garrett Winters",
#       "Accountant",
#       "Tokyo",
#       "8422",
#       "2011/07/25",
#       "$170,750"
#     ]]

#     df = pd.read_csv('static/data/2ndiat.csv')[['analyst','create_dt','iat_id','iat_name','summary_offices']]
#     seccsv = df.to_json(orient='records')


#     return render_template("test.html",sectest=sectest,seccsv=seccsv)

@app.route('/_test-json')
def test_json():
    json = [
    [
      "Tiger Nixon",
      "System Architect",
      "Edinburgh",
      "5421",
      "2011/04/25",
      "$320,800"
    ],
    [
      "Garrett Winters",
      "Accountant",
      "Tokyo",
      "8422",
      "2011/07/25",
      "$170,750"
    ]]
    # json = [{
    #     "name": "Tiger Nixon",
    #     "position": "System Architect",
    #     "salary": "$320,800",
    #     "start_date": "2011/04/25",
    #     "office": "Edinburgh",
    #     "extn": "5421"
    #   }, {
    #     "name": "Garrett Winters",
    #     "position": "Accountant",
    #     "salary": "$170,750",
    #     "start_date": "2011/07/25",
    #     "office": "Tokyo",
    #     "extn": "8422"
    #   }]
    return jsonify(json)

if __name__ == '__main__':
    app.run(debug=True)
