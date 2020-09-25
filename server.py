from flask import Flask, render_template, request, send_file, send_from_directory, safe_join, abort
import os
from postcode import postcode_checker


app = Flask(__name__)



#Randomly generate secret keys
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


#Routes to the index
@app.route("/", methods=['GET','POST'])
def index():
    show_hide = 'none'
    
    if request.method == 'POST':
        postcode = request.form['postcode']
        evaluate_postcode = postcode_checker(postcode)
        if evaluate_postcode == 'Yes':
            return render_template('booking.html')
        else:
            show_hide = 'block'
            return render_template('index.html', evaluate_postcode = evaluate_postcode, show_hide = show_hide)

        return render_template('index.html', evaluate_postcode = evaluate_postcode, show_hide = show_hide)
    else:
        return render_template('index.html', show_hide = show_hide)





if __name__== '__main__':
    app.run(debug=True)