from flask import Flask, render_template, request, url_for, redirect
from mathFuncs import Calc

a,b,c,A,B,C=2,0,0,0,0,0

app = Flask(__name__, template_folder=r'C:\Users\natha\Documents\code\Triangle Web App\Templates')

@app.route('/', methods=["POST", "GET"])
def nodir():
    if request.method == "POST":
            x = (Calc([request.form['a'], request.form['b'], request.form['c'],
                 request.form['A'], request.form['B'], request.form['C']]))
            if not isinstance(x, dict):
                return redirect(url_for("index", a = 0, b = 0, c = "Invalid Triangle", A = 0, B = 0, C = 0))
            vals = [i for i in x.values()]
            a = vals[0]
            b = vals[1]
            c = vals[2]
            A = vals[3]
            B = vals[4]
            C = vals[5]
            return redirect(url_for("index", a = a, b = b, c = c, A = A, B = B, C = C))

    else:
        return render_template('base.html')
        




@app.route("/<a>%<b>%<c>%<A>%<B>%<C>")
def index(a,b,c,A,B,C):
    # u,v,w,x,y,z = name[a], name[b], name[c], name[A], name[B], name[C]
    return render_template("slub.html", a = a, b = b, c = c, A = A, B = B, C = C)



    
app.run("0.0.0.0", port=5000, debug=True)