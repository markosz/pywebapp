from flask import Flask, request
import time


app = Flask(__name__)

def pi_digits(x): 
    """Generate x digits of Pi.""" 
    k,a,b,a1,b1 = 2,4,1,12,4 
    while x > 0:
        p,q,k = k * k, 2 * k + 1, k + 1 
        a,b,a1,b1 = a1, b1, p*a + q*a1, p*b + q*b1 
        d,d1 = a/b, a1/b1 
        while d == d1 and x > 0:
            yield int(d) 
            x -= 1 
            a,a1 = 10*(a % b), 10*(a1 % b1) 
            d,d1 = a/b, a1/b1


@app.route("/pi") 
def index():
    digits = int(request.args.get('d'))
    if digits == None:
        digits = 10

    start_time = time.time()
    res = [str(n) for n in list(pi_digits(digits))] 
    end_time = time.time()
    delta_time = end_time - start_time

    res_str=str(res.pop(0))+'.'+"".join(res)

    print_str=res_str
    if digits > 50 :
        print_str=res_str[0:50]+"..."

    return '<pre>'+print_str+ ' Time: '+str(delta_time)+'</pre>'

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8080,  debug=True)


