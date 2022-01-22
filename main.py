import os
from selenium import webdriver
from flask import  *

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

# driver = webdriver.Chrome(executable_path="../webdriver/chromedriver.exe",chrome_options=op)
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)


app = Flask(__name__)
app.secret_key = b'BB,^z\x90\x88?\xcf\xbb'


@app.route('/',methods=['GET'])
def home():
    return """
<p>Ghost Scrapper Rendered JS</p>
<footer>Coded By Ghost Saint</footer>
"""

@app.route('/scrap', methods=['GET'])
def scrap():
    if request.args.get('url'):
        url = request.args['url']
        driver.get(url)
        # print(driver.page_source)
        return driver.page_source
    else:
        return "Please Insert Url Param!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT','5000')),debug=True)
