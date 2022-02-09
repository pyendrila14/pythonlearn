from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submitForm():
    error = None
    if request.method == 'POST':
      data=request.form.to_dict()
      writeToCsv(data)
    
      return redirect('thankyou.html')
    else:
      return "what happened!!!!!!!!!!!!!!"

def writeToFile(data):
  with open("database.txt",mode="a") as database:
    email=data["email"]
    message=data["message"]
    subject=data["subject"]
    database.write(f'\n {email}, {subject}, {message}')

def writeToCsv(data):
  with open("database.csv",mode="a",newline='') as database2:
    email=data["email"]
    message=data["message"]
    subject=data["subject"]
    writer=csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([email,message,subject])
