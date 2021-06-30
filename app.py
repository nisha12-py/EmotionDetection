from flask import Flask,render_template,request
from main import detect_emotion
from main import polar_detect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/detect',methods=['POST','GET'])
def detect():
    if request.method == 'POST':
        text = request.form['message']
        # print("received")
        # print(text)
        emo = detect_emotion(text)
        # print(emo)
        pol = polar_detect(text)
        # print(pol)
        return render_template('home.html', enteredtext=text, op=1, emotion=emo,polarity=pol)

if __name__ == '__main__':
    app.run(debug=True)