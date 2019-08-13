#!/usr/bin/env python3

import tkinter
import proton
from cli_proton_python import sender
import ssl
import uuid
from proton._reactor import _generate_uuid
#imports end


#const
scheme = "amqps://"
username = "consumer@HONO"
password = "<insertYourSecretHere>"
hostAndPort = "localhost"
tenant = "rover"
device = "rover2"
topic_to_publish = "control/"+tenant+"/"+device
speed = 380
trustStore = "<pathToTrustStoreInPemFormat>"
#const end


def sendControlMsg( msg ):
	print ("sending control msg " + str(msg))
	parser = sender.options.SenderOptions()
	opts, _= parser.parse_args()
	opts.broker_url = scheme + username + ":" + password +"@"+ hostAndPort +"/"+ topic_to_publish
	opts.conn_ssl_trust_store = trustStore
	opts.conn_ssl_verify_peer = True
	opts.conn_ssl_verify_peer_name = True
	opts.msg_id = "0" # will be generated automatically
	opts.msg_subject = "RoverDriving"
	opts.msg_content = str(msg)
	opts.msg_reply_to = topic_to_publish+"/"+str(_generate_uuid())
	opts.msg_correlation_id = "null"
	opts.msg_content_type = "application/json"
	opts.log_lib = "TRANSPORT_DRV"
	opts.log_msgs = 'dict'

	container = proton.reactor.Container(sender.Send(opts))
	container.run()

#funcs

def turn_right():
	sendControlMsg( "{\"command\":\"E\",\"speed\":"+ str(speed_var.get() + 360) +" }" )
	print("turn right clicked")

def turn_right_back():
	sendControlMsg( "{\"command\":\"D\",\"speed\": "+ str(speed_var.get() + 360) +" }" )
	print("turn right back clicked")

def turn_left():
   sendControlMsg("{\"command\":\"Q\",\"speed\": "+ str(speed_var.get() + 360) +" }")
   print("turn left clicked")

def turn_left_back():
   sendControlMsg("{\"command\":\"A\",\"speed\": "+ str(speed_var.get() + 360) +" }")
   print("turn left back clicked")

def move_forward():
   sendControlMsg("{\"command\":\"W\",\"speed\": "+ str(speed_var.get() + 360) +" }")
   print("move forward clicked")

def move_back():
   sendControlMsg("{\"command\":\"S\",\"speed\": "+ str(speed_var.get() + 360) +" }")
   print("move back clicked")

def spot_right():
   sendControlMsg("{\"command\":\"K\",\"speed\": "+ str(speed_var.get() + 360) +" }")
   print("move spot right clicked")

def spot_left():
   sendControlMsg("{\"command\":\"J\",\"speed\": "+ str(speed_var.get() + 360) +" }")
   print("move spot left clicked")

def stop_move():
   sendControlMsg("{\"command\":\"F\",\"speed\": "+ str(speed_var.get() + 360) +" }")
   print("Stop clicked")

def set_speed(event):
   speed = speed_var.get() + 360
   print("set speed to", speed)
     
def showPosEvent(event):
    print("posevt")
     
def onArrowUp(event):
    move_forward() 
    print("Arrow up")

def onArrowDown(event):
    move_back()
    print("Arrow down")

def onArrowLeft(event):
    turn_left()
    print("Arrow left")

def onArrowRight(event):
    turn_right()
    print("Arrow right")

def onSpaceBar(event):
    stop_move()
    print("Spacebar pressed")


if __name__=="__main__":
    
    tkroot = tkinter.Tk()
    tkroot.title("Rover Controller")
    speed_var = tkinter.DoubleVar() #tkinter.DoubleVar()
    labelfont = ('arial', 15, 'bold')     

    #Keyboard Input           
    tkroot.bind('<Up>',onArrowUp)
    tkroot.bind('<Down>',onArrowDown)
    tkroot.bind('<Left>',onArrowLeft)
    tkroot.bind('<Right>',onArrowRight)
    tkroot.bind('<space>',onSpaceBar)
    tkroot.focus()
    #Keyboard Input End

    #Buttons
    B_right = tkinter.Button(tkroot, text =">" , command= turn_right)
    B_right.place(x = 65, y= 25, height=25, width=25)
   
    B_right_back = tkinter.Button(tkroot, text =">" , command= turn_right_back)
    B_right_back.place(x = 65, y= 55, height=25, width=25)

    B_left  = tkinter.Button(tkroot, text ="<", command= turn_left)
    B_left.place(x= 15,y = 25, height=25, width=25)

    B_left_back  = tkinter.Button(tkroot, text ="<", command= turn_left_back)
    B_left_back.place(x= 15,y = 55, height=25, width=25)

    B_up = tkinter.Button(tkroot, text ="^", command= move_forward)
    B_up.place(x= 40, y = 10 ,  height=25, width=25)

    B_down = tkinter.Button(tkroot, text ="v", command= move_back)
    B_down.place(x= 40, y = 70, height=25, width=25)

    B_stop = tkinter.Button(tkroot, text ="Stop", command= stop_move)
    B_stop.place(x = 10,y = 160 , height = 30, width=85)

    B_spot_left = tkinter.Button(tkroot, text ="<)", command= spot_left)
    B_spot_left.place(x = 100,y = 160 , height = 30, width=35)

    B_spot_right = tkinter.Button(tkroot, text =">(", command= spot_right)
    B_spot_right.place(x = 140,y = 160 , height = 30, width=35)

    speed_label = tkinter.Label(tkroot , text = "Speed")
    speed_label.place(x= 10, y = 105, height=50, width=50)

    speed_scale = tkinter.Scale(tkroot, variable = speed_var,orient = tkinter.HORIZONTAL)
    speed_scale.bind("<ButtonRelease-1>", set_speed)
    speed_scale.place(x= 60, y = 105, height=50, width=85)
    #Buttons end

    tkroot.mainloop()
