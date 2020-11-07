from flask import Flask, render_template, request, send_file, send_from_directory, safe_join, abort
import os


app = Flask(__name__)

#Randomly generate secret keys
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


#Routes to the index
@app.route("/", methods=['GET','POST'])
def index():
    show_hide = 'none'
    
    
    if request.method == 'POST':
        area_selected = request.form['area']
        if area_selected == 'Other':
            show_hide = 'block'
            evaluate_area = "Sorry, we only serve Wood Green, Chingford, and Enfield areas"
            return render_template('index.html', show_hide = show_hide, evaluate_area = evaluate_area)
        else:
            return render_template('booking.html')
    else:
        return render_template('index.html', show_hide = show_hide)
    
    
    
    

#Route to the login page
@app.route("/login", methods=['GET','POST'])
def login():
    return render_template('login.html')






#Routes to the sign up page
@app.route("/signup", methods=['GET','POST'])
def signup():
    return render_template('signup.html')


if __name__== '__main__':
    app.run(debug=True)