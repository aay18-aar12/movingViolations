from flask import Flask
import requests
import math

app = Flask(__name__)

@app.route('/all/<int:page>')
def hello_world(page):

    ko = (page*1000)-1000

    request2 = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Violations_Moving_2023/MapServer/4/query?where=1%3D1&outFields=*&outSR=4326&resultOffset='+str(ko) +'&f=json')

    return request2.json()


@app.route('/issue_time/<string:issue_time>/<int:page>')
def retTime(issue_time, page):

    
    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Violations_Moving_2023/MapServer/4/query?where=ISSUE_TIME%3D%27' + issue_time + '%27&outFields=*&outSR=4326&resultOffset='+str(ko) +'&f=json')
    bo = request.json()
    return bo
    


@app.route('/fine/<string:fine_amount>/<int:page>')
def retFine(fine_amount, page):

    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Violations_Moving_2023/MapServer/4/query?where=FINE_AMOUNT%3D%27' + fine_amount + '%27&outFields=*&outSR=4326&resultOffset='+str(ko) +'&f=json')
    bo = request.json()
    return bo
    

@app.route('/total/<string:total>/<int:page>')
def retTotal(total, page):
    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Violations_Moving_2023/MapServer/4/query?where=TOTAL_PAID%3D%27' + total + '%27&outFields=*&outSR=4326&resultOffset='+str(ko) +'&f=json')
    bo = request.json()
    return bo

@app.route('/health')
def retHealth():
    return 'Web Service is Working'
