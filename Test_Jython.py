# Java functionality 
from java.awt import Color
from java.awt.event import ActionListener
from java.awt.event import KeyAdapter
from java.awt.event import MouseAdapter
from java.lang import System
from javax.swing import JFrame
from javax.swing import JPanel
from javax.swing import Timer
from pythonfrp.Engine import *
from reactive2D import *

# ExternalEvents is the event dictionary used by the engine.
externalEvents = {}
# LocalTime and World Objects are in Globals


# This is Jython code to interface with mouse events
class MA(MouseAdapter):
    def __init__(self, clicker):
        self.clicker = clicker
    def mouseClicked(self, event):
        self.clicker(event.getX(), event.getY())
        
class KA(KeyAdapter):
    def __init__(self, clicker):
        self.clicker = clicker
    def keyTyped(self, event):
        print("Key Pressed: " + str(event.getKeyChar()))
        self.clicker(event.getKeyChar())

# This is Jython code to interface with a graphics panel
class Canvas(JPanel):
    def __init__(self, drawer, click):
        super(Canvas, self).__init__()
        self.drawer = drawer
        self.click = click
#        self.key = key
    self.addMouseListener(MA(lambda x, y: self.click(x, y)))

def paint(self, g):
    JPanel.paint(self, g)
    self.drawer(g)

# This creates the drawing frame (Example is a stupid name ...)
class Example(JFrame, ActionListener):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

# Paint all of the objects in screenObjects
    def mypaint(self, g):
        for object in screenObjects:
            object(g)
            
# Add an external event on a mouse click
    def myclick(self, x, y):
        externalEvents['LeftMouseButton'] = SP2(x, y)   #SP2 inherited from pythonfrp StaticNumerics.py
    def mykey(self, k):
        externalEvents['KeyTyped'] = string(k)

    def initUI(self):
        self.addKeyListener(KA(lambda k: k))
        self.xp = 0
        self.yp = 0
        self.canvas = Canvas(lambda g:self.mypaint(g), lambda x, y: self.myclick(x, y))
        self.canvas.setBackground(Color(200, 200, 100))
        self.getContentPane().add(self.canvas)
        self.setTitle("Ball")
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setSize(300, 300)
        self.setLocationRelativeTo(None)
        self.setBackground(Color(255, 255, 255))
        self.setVisible(True)
        self.timer = Timer(50, self)
        self.timer.start()

# This is the heartbeat handling code - this is attached to a timer in the frame      
    def actionPerformed(self, e):
        currentTime = System.currentTimeMillis()
        del screenObjects[:]
#        print(currentTime-startTime[0])
#        print('Objects: ' + str(Globals.worldObjects))
    heartbeat((currentTime - startTime[0]) / 1000.0, externalEvents)
    externalEvents.clear()
    self.repaint()

# This is the start function that initializes the reactive engine and then starts the animation
def start():
    print("Starting...")
    startTime[0] = System.currentTimeMillis()
    initialize(0)
    Example()

# From here on this is user code - create a moving circle on each mouse click that starts from the position of the click

def makeCircle(m, v):
    circle(p2(localTime * 50 + v.x, localTime * 50 + v.y)) #localtime inherited from pythonfrp functions.py 183

def makeSquare(m, v):
    square(p2(localTime * 50 + v.x, localTime * 50 + v.y)) #localtime inherited from pythonfrp functions.py 183
    
def makeTriangle(m, v):
    triangle(p2(localTime * 50 + v.x, localTime * 50 + v.y)) #localtime inherited from pythonfrp functions.py 183
    
def typeKey(m, v):
    print(string(v.k))


    
#def checkValidKey(s):
#    if s in keyRenamings:
#        return keyRenamings[s]
#    if type(s) is type("s"):
#        if len(s) == 1 or s in allKeyNames:      CODE FROM REACTIVEPANDA EXTERNALS.PY
#            return s
#    Errors.badKeyName(s)
#allKeyNames = ["escape", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "space"]
#
#keyRenamings = {"upArrow": "arrow_up", "downArrow": "arrow_down",
#    "leftArrow": "arrow_left", "rightArrow": "arrow_right"}  





# These methods handle signals from the GUI
    # Cache keypress events so there's no duplication of key events - not
    # sure this is useful but it can't hurt.  Probably not a good idea to
    # have multiple accepts for the same event.
  

# React to each mouse press by creating a new shape
react(lbp(), makeSquare)    #inherited from reactive2d Events2D 
react(kT(), typeKey)    #inherited from reactive2d Events2D 

# Start!
start()