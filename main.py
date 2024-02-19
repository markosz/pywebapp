from decimal import *
import subprocess 
from flask import Flask, request
#from subprocess import Popen, PIPE 
from subprocess import check_output
import time


app = Flask(__name__)

def calc_pi(reps):
    getcontext().prec = reps
    result = Decimal(3.0)
    op = 1
    n = 2
    for n in range(2, 2*reps+1, 2):
        result += 4/Decimal(n*(n+1)*(n+2)*op)
        op *= -1
    return result

def get_shell_script_output_using_check_output(): 
    stdout = check_output(['./bc.sh 500']).decode('utf-8')
    return stdout


@app.route("/pi") 
def index():
    digits = int(request.args.get('d'))
    if digits == None:
        digits = 10
    start_time = time.time()
    res = calc_pi(digits)
    end_time = time.time()
    delta_time = end_time - start_time
    fmtd = "{0:.50f}".format(res)

    return '<pre>'+str(res)+' ' +fmtd+ ' Time: '+str(delta_time)+'</pre>'
    #return "Congratulations, it's a web app!"

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8080,  debug=True)


