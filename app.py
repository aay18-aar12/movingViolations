from flask import Flask
import requests
import math

app = Flask(__name__)

@app.route('/all/<int:page>')
def hello_world(page):

    ko = (page*1000)-1000

    request2 = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Violations_Moving_2023/MapServer/4/query?where=1%3D1&outFields=*&outSR=4326&resultOffset='+str(ko) +'&f=json')

    return request2.json()


@app.route('/violation/<string:code>/<int:page>')
def retTime(code, page):

    
    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Violations_Moving_2023/MapServer/4/query?where=VIOLATION_CODE%3D%27' + code + '%27&outFields=*&outSR=4326&resultOffset='+str(ko) +'&f=json')
    bo = request.json()
    return bo
    

@app.route('/agency/<string:code>/<int:page>')
def retFine(code, page):

    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Violations_Moving_2023/MapServer/4/query?where=ISSUING_AGENCY_CODE%3D' + code + '&outFields=*&outSR=4326&resultOffset='+str(ko) +'&f=json')
    bo = request.json()
    return bo

@app.route('/health')
def retHealth():
    return 'Web Service is Working'
