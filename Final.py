#!/usr/bin/env python
import sys
import plotly.plotly as py
import plotly.tools as tls 
from plotly.graph_objs import *
import numpy as np
import datetime 
import time 
py.sign_in("jpablochr", "07zun1j1j0")
galileo_path = "/media/mmcblk0p1/";
if galileo_path not in sys.path:
    sys.path.append(galileo_path);

from pyGalileo import *

tls.set_credentials_file(stream_ids=[
        "4ho4b7tare",
		"z56am2okg7",
		"eu0aosa3dh"
    ]);
stream_ids = tls.get_credentials_file()['stream_ids'];

sensorPin0 = A0;    # select the input pin for the Analog Input 1
sensorPin1 = A1;    # select the input pin for the Analog Input 2
sensorPin2 = A2;    # select the input pin for the Analog Input 3
ledPin = 13;      # select the pin for the LED
sensorValue0 = 0;  # variable to store the value coming from the sensor 1
sensorValue1 = 0;  # variable to store the value coming from the sensor 2
sensorValue2 = 0;  # variable to store the value coming from the sensor 3
Data1 = 'data1';
Data2 = 'data2';
Data3 = 'data3';
Time = 'Time';
temp = '';
pinMode(ledPin, OUTPUT); 
  
def grabartxt(var,archivo):
	archi=open(archivo + '.txt','a');
	if(archivo == Time):
		a = var + " ";
	else:
		a = str(var) + " ";
	archi.write(a);
	archi.close();


trace1 = Scatter(
    x=[],
    y=[],
    mode='lines',
	line=Line(color='rgba(50,50,50)'),
    stream=Stream(token=stream_ids[0],maxpoints=40)         # (!) embed stream id, 1 per trace
);

trace2 = Scatter(
    x=[],
    y=[],
    mode='lines',
	line=Line(color='rgba(100,100,100)'),
    stream=Stream(token=stream_ids[1],maxpoints=40)       # (!) embed stream id, 1 per trace
);
trace3 = Scatter(
    x=[],
    y=[],
    mode='lines',
	line=Line(color='rgba(200,200,200)'),
    stream=Stream(token=stream_ids[2],maxpoints=40)       # (!) embed stream id, 1 per trace
);
data = Data([trace1,trace2,trace3]);
layout = Layout(title='Time Series');

# Make a figure object
fig = Figure(data=data, layout=layout);

# (@) Send fig to Plotly, initialize streaming plot, open new tab
unique_url = py.plot(fig, filename='Embedidos');

s1 = py.Stream(stream_ids[0]);
s2 = py.Stream(stream_ids[1]);
s3 = py.Stream(stream_ids[2]);
# (@) Open the stream
s1.open();
s2.open();
s3.open();
i = 0;    # a counter
k = 5;    # some shape parameter
N = 200;  # number of points to be plotted

# Delay start of stream by 5 sec (time to switch tabs)
time.sleep(5); 

while i>-1:
    #global sensorValue0;
    #global sensorValue1;
    #global sensorValue2;
    #global Data1;
    #global Data2;
    #global Data3;
    #global Time;
  # read the value from the sensors:
    x=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    sensorValue0 = analogRead(sensorPin0);
    sensorValue1 = analogRead(sensorPin1);
    sensorValue2 = analogRead(sensorPin2);
    grabartxt(sensorValue0,Data1);
    grabartxt(sensorValue1,Data2);
    grabartxt(sensorValue2,Data3);
    grabartxt(time.strftime("%c"),Time);
  # turn the ledPin on
    digitalWrite(ledPin, HIGH);  
  # stop the program for <sensorValue0> milliseconds:
    delay(sensorValue2);          
  # turn the ledPin off:        
    digitalWrite(ledPin, LOW);   
  # stop the program for for <sensorValue0> milliseconds:
  #print("sensorValue 1:" + str(sensorValue0));
    delay(sensorValue2);
    
    # (-) Both x and y are numbers (i.e. not lists nor arrays)
    
    # (@) write to Plotly stream!
    s1.write(dict(x=x,y=sensorValue0));
    s2.write(dict(x=x,y=sensorValue1));
    s3.write(dict(x=x,y=sensorValue2));
    
            
    time.sleep(0.08);  # (!) plot a point every 80 ms, for smoother plotting
    
# (@) Close the stream when done plotting
s1.close();
s2.close();
s3.close();
