from flask import Flask, render_template

app= Flask(__name__)

@app.route('/') #home
def home():
    return render_template("EXAMhome.html")

@app.route('/visualisation', methods=['GET','POST']) #methods=['GET','POST'] untuk memindah page
def about():
    return render_template('EXAMvisualisation.html')

@app.route('/dataset', methods=['GET','POST']) #methods=['GET','POST'] untuk memindah page
def dataset():
    return render_template('EXAMdataset.html')

@app.route('/back', methods=['GET','POST']) #methods=['GET','POST'] untuk memindah page
def back():
    return render_template('EXAMhome.html')



if __name__ == '__main__':
    app.run(debug=True)