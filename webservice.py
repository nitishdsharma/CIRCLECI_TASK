"""
    Filename : webservice.py
    Application : REST APIs
    Problem statement : Create a merged API having name and chuck norris joke
"""

# Program Metadata
_author_ = 'Nitish Sharma'
_maintainer_ = 'Nitish Sharma'
_email_ = 'nitish.sharma@calsoftinc.com'
_status_ = 'Automation'

#print(__author__)

#Importing the used libraries
from flask import Flask, request
import requests, json, jsonpath

#Defining the global variables
name_url = 'http://uinames.com/api/'
p_joke_url = 'http://api.icndb.com/jokes/random'

#Defining methods
def getting_name():
    r_name = requests.get(name_url)
    r_name_json = json.loads(r_name.content)
    first_name = jsonpath.jsonpath(r_name_json, 'name')
    second_name = jsonpath.jsonpath(r_name_json, 'surname')
    r_name = (first_name[0],second_name[0])
    return r_name

def getting_joke(r_name):
    if len(r_name) == 2:
        first_name = r_name[0]
        second_name = r_name[1]
    else:
        first_name = ''
        second_name = ''
    param_string = '?firstName=%s&lastName=%s&limitTo=\[nerdy\]' %(first_name,second_name)
    joke_url = p_joke_url + param_string
    r_joke = requests.get(joke_url)
    r_joke_json = json.loads(r_joke.content)
    r_joke = jsonpath.jsonpath(r_joke_json,'value.joke')
    return r_joke[0]

# Create the application instance
fl_object = Flask(__name__)
#Binds the URL to the function
@fl_object.route("/", methods=['GET'])
def merge_webservice():
    # defining name and joke objects
    r_name = getting_name()
    joke = getting_joke(r_name)
    object = [r_name,joke]
    return (str(object))

# Handle 404 - Not Found
@fl_object.errorhandler(404)
def page_not_found(e):
    """ For Handling 404 - Not Found"""
    return "Resource / Page Not Found : {}".format(e)

# Handle 500 - Internal server Error
@fl_object.errorhandler(500)
def page_not_found(e):
    """ For Handling 500 - Internal server error"""
    return "500 Internal server error : {}".format(e)

#Program execution startpoint
if __name__ == "__main__":
    try:
        #Running application on local server
        #host 0.0.0.0 is a no particular ip address which can be replaced by any other host IP/username of that machine
        #https://www.howtogeek.com/225487/what-is-the-difference-between-127.0.0.1-and-0.0.0.0/
        fl_object.run(debug=True, host='0.0.0.0', port=5000)
    except page_not_found as e:
        print(e)
        raise Exception('Unable to start webserver ', e)
