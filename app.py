import os
import datetime
import socket
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    
    version = 0.17
    hostname = socket.gethostname()
    time = datetime.datetime.now()
    message = 'Goodbye and thanks for all the fish!'
    
    name = 'Mark'
    try:
        name = os.environ['NAME']
    except KeyError:
        name = 'Flask-demo'
    
    return render_template('hello.html',
                           message=message,
                           hostname=hostname,
                           time=time ,
                           version=version,
                           name=name)


if __name__ == '__main__':

    app.run(host='0.0.0.0')
    # app.run(debug=True, host='0.0.0.0')
