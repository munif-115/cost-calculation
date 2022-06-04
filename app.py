from flask import Flask, render_template,request
#import jsonify
import requests
#import pickle
##import numpy as np
#import sklearn
app = Flask(__name__)
#model = pickle.load(open('heartattack.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
     if request.method == 'POST':
          val= int(request.form['val'])
          hawb = float(request.form['hawb'])
          cw=int(request.form['cw'])
          gw=int(request.form['gw'])
          price=int(request.form['cost'])
          if val==1:
              freightcw=price
              awcmawb=2.10
              thccw=0.08
              sscgw=0.06
              mbcw=0.04
              amshawb=10
              freightcw2=float(cw)*float(freightcw)
              thccw2=float(cw)*float(thccw)
              sscgw2=float(sscgw)*float(gw)
              mbcw2=float(mbcw)*float(gw)
              amshawb2=float(hawb)*float(amshawb)
              amshawb3=amshawb2+10
              tcost=freightcw2+awcmawb+thccw2+sscgw2+mbcw2+amshawb3
          elif val==2:               
                freightcw=price
                awchawb=3
                thccw=0
                sscgw=0
                mb=0
                ams=10
                freightcw2=float(cw)*float(freightcw)
                thccw2=float(cw)*float(thccw)
                sscgw2=float(sscgw)*float(gw)
                mbgw2=float(mb)*float(gw)
                amshawb2=float(hawb)*float(ams)
                tcost=freightcw2+awchawb+thccw2+sscgw2+mbgw2+amshawb2
          elif val==3:   
                freightcw=price
                awchawb=2.10
                thccw=0
                sscgw=0
                mbcw=0
                ams=10
                freightcw2=float(cw)*float(freightcw)
                thccw2=float(cw)*float(thccw)
                sscgw2=float(sscgw)*float(gw)
                mbgw2=float(mbcw)*float(gw)
                amshawb2=float(hawb)*float(ams)
                tcost=freightcw2+awchawb+thccw2+sscgw2+mbgw2+amshawb2
          elif val==4:  
              freightcw=price
              awchawb=15
              thccw=0.08
              sscgw=0.06
              fsccw=0.75
              sccw=0.25
              ams=10
              freightcw2=float(cw)*float(freightcw)
              thccw2=float(cw)*float(thccw)
              sscgw2=float(sscgw)*float(gw)
              fsccw2=float(fsccw)*float(cw)
              sccw2=float(sccw)*float(cw)
              tcost=freightcw2+awchawb+thccw2+sscgw2+fsccw2+sccw2+ams
          elif val==5: 
               freightcw=price
               awcmawb=2.10
               thccw=0.08
               sscgw=0.06
               #mbcw=0.04
               myccw=0.85
               amshawb=10
               freightcw2=float(cw)*float(freightcw)
               thccw2=float(cw)*float(thccw)
               sscgw2=float(sscgw)*float(gw)
               myccw2=float(myccw)*float(cw)
               amshawb2=float(hawb)*float(amshawb)
               tcost=freightcw2+awcmawb+thccw2+sscgw2+myccw2+amshawb2
          elif val==6: 
              freightcw=price
              awcmawb=0
              thccw=0.08
              sscgw=0.08
              #mbcw=0.04
              myccw=0
              amshawb=10
              freightcw2=float(cw)*float(freightcw)
              thccw2=float(cw)*float(thccw)
              sscgw2=float(sscgw)*float(gw)
              myccw2=float(myccw)*float(cw)
              amshawb2=float(hawb)*float(amshawb)
              tcost=freightcw2+awcmawb+thccw2+sscgw2+myccw2+amshawb2
          elif val==7:
              freightcw=price
              awc=10
              thccw=0.08
              #sscgw=0.08
              sscgw=0.08
              rhdcw=0.02
              amshawb=10
              freightcw2=float(cw)*float(freightcw)
              thccw2=float(cw)*float(thccw)
              xbcgw2=float(sscgw)*float(gw)
              rhdcw2=float(rhdcw)*float(cw)
              amshawb2=float(hawb)*float(amshawb)
              tcost=freightcw2+awc+thccw2+ sscgw2+ rhdcw2+amshawb2
          elif val==8:
              freightcw=price
              awchawb=2.10
              thccw=0.08
              sscgw=0.06
              mbgw=0
              amshawb=13
              freightcw2=float(cw)*float(freightcw)
              thccw2=float(cw)*float(thccw)
              sscgw2=float(sscgw)*float(gw)
              mbgw2=float(mbgw)*float(gw)
              #amshawb2=float(hawb)*float(amshawb)
              #amshawb3=amshawb2+10
              tcost=freightcw2+awchawb+thccw2+sscgw2+mbgw2+amshawb
          elif val==9:
              freightcw=price
              awcmawb=0
              thccw=0.10
              sscgw=0.08
              fccw=0.49
              amshawb=10
              freightcw2=float(cw)*float(freightcw)
              thccw2=float(cw)*float(thccw)
              sscgw2=float(sscgw)*float(gw)
              fccw2=float(fccw)*float(cw)
              amshawb2=float(hawb)*float(amshawb)
              amshawb3=amshawb2+12
              tcost=freightcw2+awcmawb+thccw2+sscgw2+fccw2+amshawb3
              
         
     return render_template('index.html',cost="The total cost is {}".format(tcost),price="THC/CW:{}".format(thccw),ssc="SSC/GW:{}".format(sscgw))
              
              
              
     #else:
       #return render_template('index.html')







if __name__=="__main__":
    app.run(debug=True,use_reloader=False)