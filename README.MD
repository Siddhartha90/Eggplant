##Setup

###
(Assumes python3 is installed)

pip3 install google-search-results

python3 -m flask --app app run

If you run into OpenSSL issues, try:
pip3 install urllib3==1.26.6

pip3 install openai

Before running, set environment variable:

export api_key=<keyhere>