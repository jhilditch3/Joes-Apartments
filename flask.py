from flask import Flask, request, redirect, render_template
import random
import json
import boto3

AWSKEY = '' # removed for privacy
AWSSECRET = ''# removed for privacy
PUBLIC_BUCKET = ""# removed for privacy
STORAGE_URL = ""# removed for privacy

app = Flask(__name__)

def get_public_bucket():
    s3 = boto3.resource(service_name = "s3",
    region_name = 'us-east-1',
    aws_access_key_id = AWSKEY,
    aws_secret_access_key=AWSSECRET)

    bucket = s3.Bucket(PUBLIC_BUCKET)

    return bucket

@app.route('/listfiles')
def listfiles():
    bucket = get_public_bucket()
    items = []
    for item in bucket.objects.all():
        items.append(item.key)
    return{"url" : STORAGE_URL, "items": items}

@app.route('/hello')
def hello_world():
    return 'Hello from Joe'

@app.route('/add')
def add():
    a = request.args.get('a')
    b = request.args.get('b')
    total = int(a) + int(b)
    return str(total)

@app.route('/catalog/<search>')
def catalog(search):
    f = open("/home/Jhilditch/data/courses.json")
    courses = json.load(f)
    f.close()
    result_list = []
    for c in courses:
        if c['number'].lower().startswith(search.lower()) or search.lower() in c['name'].lower():
            result_list.append(c)
    return { "result" : result_list}

def find_course(number):
    f = open("/home/Jhilditch/data/courses.json")
    courses = json.load(f)
    f.close()
    number = number.lower()
    for c in courses:
        if number == c['number'].lower():
            return c
    return {"name" : "unknown", "description" : "unknown", "credits" : 0}

@app.route('/course/<number>')
def course(number):
    c = find_course(number)
    return render_template("course.html", course = c)

@app.route('/seidenberg')
def seidenberg():
    return redirect('https://www.pace.edu/seidenberg')

@app.route('/account')
def account():
    logged_in = False
    if not logged_in:
        return redirect('/hello')
    return "hey"

@app.route('/apartment')
def apartment():

    return render_template("apartments.html")

@app.route('/aptsearch/<search>/<beds>/<sort>')
def aptsearch(search, beds, sort):
    f = open("/home/Jhilditch/data/apartments.json")
    apartments = json.load(f)
    f.close()
    result_list = []
    beds = int(beds)
    sort = int(sort)
    # filter
    for a in apartments:
        if search.lower() in a['title'].lower():
            if beds <= a["bedrooms"]:
                result_list.append(a)

    if sort == 1: #Ascending order
        sorted_results = sorted(result_list, key = lambda x: x["rent"])

    elif sort == 2: #Descending order
        sorted_results = sorted(result_list, key = lambda x: x["rent"], reverse=True)

    elif sort == 0:
        return {"result" : result_list}

    return { "result" : sorted_results}
