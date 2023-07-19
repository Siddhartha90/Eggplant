https://devpost.com/software/the-aubergine-index

Done as part of the [Climate AI Hackathon](https://lu.ma/aixclimate) | SF #TechWeek.

## Setup

(Assumes python3 is installed)

pip3 install google-search-results

python3 -m flask --app app run

If you run into OpenSSL issues, try:
pip3 install urllib3==1.26.6

pip3 install openai

Before running, set environment variable:

export api_key=<keyhere>
