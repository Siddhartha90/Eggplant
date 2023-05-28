from flask import Flask, redirect, url_for, request
from serpapi import GoogleSearch

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test/<name>")
def test(name):
    return "<p>Hello " + name + "!</p>"

@app.route("/test2/<name>")
def test2(name):
    return "<p>Hello2 " + name + "!</p>"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('test', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('test', name=user))

######################

@app.route("/reviews/<name>/<results>")
def reviews(name, results):
    return "<p>Reviews for business: " + name + "</br>" + results + "</p>"        

# Uses https://serpapi.com/google-maps-api to first fetch the place
@app.route('/getReviews', methods=['POST', 'GET'])
def getReviews():
    if request.method == 'POST':
        business = request.form['business']
        params = {
          "engine": "google_maps",
          "q": business,
          "ll": "@37.809326,-122.409981,10.1z",
          "type": "search",
          "api_key": "b37d293807a175ad5d3f548b99d2552c5961eb8067f8350312b48aca2c1a9db6",          
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        # print(results)
        first_result = results["place_results"] # Should contain just one result unless this is an SF chain, in which case we just pick the first.
        print(first_result)
        restaurantId = first_result["data_id"] # this will be used to query for reviews
        # organic_results = ["2" for x in range(5)]
        # return redirect(url_for('reviews', name=user, results=organic_results))
        return "<p>Reviews for business: " + business + " and id - " + restaurantId + "</br>" + str(results) + "</p>"        
    else:
        # log error
        return

 
if __name__ == '__main__':
    app.run(debug=True)