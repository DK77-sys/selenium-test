import os
from selenium import webdriver
from flask import  *

op = webdriver.ChromeOptions()
op.binary.location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
source)


app = flask.Flask(__name__)
app.secret_key = b'BB,^z\x90\x88?\xcf\xbb'

@app.route('/', methods=['GET'])
def home():
    url = request.args['url']
    d = driver.get(url)
    result = d.page_source
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT','5000')),debug=True)
