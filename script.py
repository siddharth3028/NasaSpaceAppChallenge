from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
   return"""Hello Guys,

I am Siddharth Jadhav.I have completed my B.E. in Computer Science in 2020.

I am feeling honour to serve myself for NASA through my contribution.

I have some analysis report which I have completed during this event and I wanted showcase that in front of you guys.

This are the things which I have researched and I hope you will give your valubale time thank you !


Regards,
Siddharth Jadhav"""

if __name__=="__main__":
    app.run(debug=True)
