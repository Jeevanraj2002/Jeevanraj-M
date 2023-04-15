import flask
model = pickle.load (open ('flight.pkl', 'rb'))
app = flask(__name__)
@app.route('/')

def home():
    return render_template("index.html")
    @app.route('/prediction', methods = ['POST'])
def predict():
    name = print['name']
    month = ['month']
    dayofmonth = ['dayofmonth']
    dayofweek= ['dayofweek']
    origin = ['origin']
    if(origin == "msp"):
        origin1,origin2,origin3,origin4,origin5 = 0,0,0,0,1
    if(origin == "dtw"):
        origin1,origin2,origin3,origin4,origin5 = 1,0,0,0,0
    if(origin == "jfk"):
        origin1,origin2,origin3,origin4,origin5 = 0,0,1,0,0
    if(origin == "sea"):
        origin1,origin2,origin3,origin4,origin5 = 0,1,0,0,0
    if(origin == "alt"):
        origin1,origin2,origin3,origin4,origin5 = 0,0,0,1,0
        destination = request.form['destination']
    if destination == "msp":
        destinationl,destination2,destination3,destination4,destination5 = 0,0,0,0,1
    if destination == "dtw":
        destinationl,destination2,destination3,destination4,destination5 = 1,0,0,0,0
    if destination == "jfk":
       destinationl,destination2,destination3,destination4,destination5 = 0,0,1,0,0
    if destination == "sea":
        destinationl,destination2,destination3,destination4,destination5 = 0,1,0,0,0
    if destination == "alt":
        destinationl,destination2,destination3,destination4,destination5 = 0,0,0,1,0
    dept = request.form['dept']
    arrtime = request.form['arrtime']
    actdept = request.form['actdept']
    dept15 = int(dept)-int(actdept)
    total = [[name,month,dayofmonth,dayofweek,origin1,origin2,origin3,origin4,origin5,destinationl,destination2,destination3,destination5,dept,arrtime,actdept]]
    y_predict =  model.predict(total)
    print(y_predict)
    if y_predict == [0.]:
        ans="The Flight will be on time"
    else:
        ans="The Flight will be delayed"
        return render_template("index.html",showcase=ans)
if __name__=='__main__':
    app.run(debug = true)