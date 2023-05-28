from flask import Flask, render_template, redirect, url_for, request
from serpapi import GoogleSearch
from fetchReviews import fetchReviews

app = Flask(__name__, template_folder='')

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
        keyword = request.form['keyword']
        params = {
          "engine": "google_maps",
          "q": business,
          "ll": "@37.809326,-122.409981,10.1z",
          "type": "search",
          "api_key": "b37d293807a175ad5d3f548b99d2552c5961eb8067f8350312b48aca2c1a9db6",          
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        first_result = results["place_results"] # Should contain just one result unless this is an SF chain, in which case we just pick the first.
        restaurantId = first_result["data_id"] # this will be used to query for reviews
        result = fetchReviews(restaurantId, 5, keyword)
        sentimentArray = result["sentiment"]
        print(sentimentArray)
        if "reasoning" in sentimentArray:
            reason = sentimentArray["reasoning"]
        if "reasons" in sentimentArray:
            reason = sentimentArray["reasons"]
        if "reason" in sentimentArray:
            reason = sentimentArray["reason"]
        if "explanation" in sentimentArray:
            reason = sentimentArray["explanation"]
        sentiment = sentimentArray["sentiment"]
        if reason is not None:
            return render_template('result.html', keyword=keyword, message=sentiment, reason = reason)
        else:
            return render_template('result.html', keyword=keyword, message=sentiment)
    else:
        # log error
        return

 
if __name__ == '__main__':
    app.run(debug=True)