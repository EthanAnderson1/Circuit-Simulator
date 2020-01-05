#pygame import allows the window to be opened 
#allows for the position and buttons on the mouse to be recorded
#and words, shapes and images to be display
import pygame
#the tkiner and tkmessagebox allows the pop up notifications
import tkinter
from tkinter import messagebox
pygame.init()

#---------------------------------------------------------------------------#

#Created a class where all of the variables will be stored for the circuit
class basewire(object):
    def __init__(self):
# this is how the varibales are stored and this is repeated for
# each side of the circuit
# [series voltage, parallel voltage, series current,
# parallel current, series resistance,
# parallel resistance series bulb, parallel bulb, powersupply]
# the last part of the list is the total amount of powersupplies
# added to the circuit
        self.Variables = [[0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],0.0]  
        self.componentselected = 0

#---------------------------------------------------------------------------#
        
# Inheritance classes

# Takes varibale from the basewire class
# and creates a power variable and
# creates and updates varibales for each side of the circuit
# each of these sub classes checks if there is a parallel wire
# involved in the calculations then handles the data acordingly
# using ohms law and
# 1/Parallel Circuits Resistance = 1/R1 + 1/R2

# the update procedure updates all of the variables
# during the running of the program
class leftwire(basewire):
    def __init__(self):
        super(leftwire, self).__init__()
        if self.Variables[0][5] > 0:
            self.leftresistance = 1/((1/self.Variables[0][5])+(1/self.Variables[0][4]))
        else:
            self.leftresistance = self.Variables[0][4]
        self.leftvoltage = 0.0
        self.leftcurrent = 0.0
        self.lspower = ((self.Variables[0][2]**2))*(self.Variables[0][4])
        self.lppower = ((self.Variables[0][3]**2))*(self.Variables[0][5])
    def updateleftwire(self):
        if self.Variables[0][5] > 0:
            self.leftresistance = 1/((1/self.Variables[0][5])+(1/self.Variables[0][4]))
            self.Variables[0][3] = self.leftvoltage/self.Variables[0][5]
        else:
            self.leftresistance = self.Variables[0][4]
        self.Variables[0][2] = self.leftvoltage/self.Variables[0][4]
        self.lspower = ((self.Variables[0][2]**2))*(self.Variables[0][4])
        self.lppower = ((self.Variables[0][3]**2))*(self.Variables[0][5])
class bottomwire(basewire):
    def __init__(self):
        super(bottomwire, self).__init__()
        if self.Variables[3][5] > 0:
            self.bottomresistance = 1/((1/self.Variables[3][5])+(1/self.Variables[3][4]))
        else:
            self.bottomresistance = self.Variables[3][4]
        self.bottomvoltage = 0.0
        self.bottomcurrent = 0.0
        self.bspower = ((self.Variables[3][2]**2))*(self.Variables[3][4])
        self.bppower = ((self.Variables[3][3]**2))*(self.Variables[3][5])

    def updatebottomwire(self):
        if self.Variables[3][5] > 0:
            self.bottomresistance = 1/((1/self.Variables[3][5])+(1/self.Variables[3][4]))
            self.Variables[3][3] = self.bottomvoltage/self.Variables[3][5]
        else:
            self.bottomresistance = self.Variables[3][4]
        self.Variables[3][2] = self.bottomvoltage/self.Variables[3][4]
        self.bspower = ((self.Variables[3][2]**2))*(self.Variables[3][4])
        self.bppower = ((self.Variables[3][3]**2))*(self.Variables[3][5])
class rightwire(basewire):
    def __init__(self):
        super(rightwire, self).__init__()
        if self.Variables[1][5] > 0:
            self.rightresistance = 1/((1/self.Variables[1][5])+(1/self.Variables[1][4]))
        else:
            self.rightresistance = self.Variables[1][4]
        self.rightvoltage = 0.0
        self.rightcurrent = 0.0
        self.rspower = ((self.Variables[1][2]**2))*(self.Variables[1][4])
        self.rppower = ((self.Variables[1][3]**2))*(self.Variables[1][5])
    def updaterightwire(self):
        if self.Variables[1][5] > 0:
            self.rightresistance = 1/((1/self.Variables[1][5])+(1/self.Variables[1][4]))
            self.Variables[1][3] = self.rightvoltage/self.Variables[1][5]
        else:
            self.rightresistance = self.Variables[1][4]
        self.Variables[1][2] = self.rightvoltage/self.Variables[1][4]
        self.rspower = ((self.Variables[1][2]**2))*(self.Variables[1][4])
        self.rppower = ((self.Variables[1][3]**2))*(self.Variables[1][5])
class topwire(basewire):
    def __init__(self):
        super(topwire, self).__init__()
        if self.Variables[2][5] > 0:
            self.topresistance = 1/((1/self.Variables[2][5])+(1/self.Variables[2][4]))
        else:
            self.topresistance = self.Variables[2][4]
        self.topvoltage = 0.0
        self.topcurrent = 0.0
        self.tspower = ((self.Variables[2][2])**(2))*(self.Variables[2][4])
        self.tppower = ((self.Variables[2][3]**2))*(self.Variables[2][5])
    def updatetopwire(self):
        if self.Variables[2][5] > 0:
            self.topresistance = 1/((1/self.Variables[2][5])+(1/self.Variables[2][4]))
            self.Variables[2][3] = self.topvoltage/self.Variables[2][5]
        else:
            self.topresistance = self.Variables[2][4]
        self.Variables[2][2] = self.topvoltage/self.Variables[2][4]
        self.tspower = ((self.Variables[2][2]**2))*(self.Variables[2][4])
        self.tppower = ((self.Variables[2][3]**2))*(self.Variables[2][5])
# combines all of the variables to make variables for the circuit as a whole
# this class containes all of the procedures for the program
class wire(topwire, rightwire, bottomwire, leftwire, basewire):
    def __init__(self):
        super(wire,self).__init__()
        self.resistance = self.topresistance + self.rightresistance + self.leftresistance + self.bottomresistance
        self.current = self.Variables[4] /self.resistance
        self.power = (self.Variables[4] **2)/self.resistance

    def updatecircuit(self):
        self.resistance = self.topresistance + self.rightresistance + self.leftresistance + self.bottomresistance
        self.current = self.Variables[4] /self.resistance
        self.power = (self.Variables[4] **2)/self.resistance
        self.leftvoltage = self.current * self.leftresistance
        self.rightvoltage = self.current * self.rightresistance
        self.topvoltage = self.current * self.topresistance
        self.bottomvoltage = self.current * self.bottomresistance
        self.updateleftwire()
        self.updaterightwire()
        self.updatetopwire()
        self.updatebottomwire()        

#---------------------------------------------------------------------------#

    # this function makes the pop up notifications
    def msg(self, m):
        # this closes an unnessasary window opened by tkmessagebox
        window = tkinter.Tk()
        window.wm_withdraw()
        #this makes the actual pop up window
        messagebox.showinfo(title="Circuit Simulator", message=m)

#---------------------------------------------------------------------------#
        
    # this function writes on the screen, m= message, c= colour, x,y= coordinates
    def write(self, m,c,x,y):
        t = font.render(m, True, (c))
        screen.blit(t, (x, y))

#---------------------------------------------------------------------------#
        
    # this function makes writes on on the screen, t= image file name, x,y= coordinates
    def displayimage(self, t,x,y):
        u = pygame.image.load(t)
        screen.blit(u, (x, y))

#---------------------------------------------------------------------------#
        
    # function that handles the mouse inputs 
    def mousefunction(self, mouseposx, mouseposy, mouseclick):
        global circuitnumber
        global circuitsleft
        
    #   When the Mouse is at the bulb
        if 1315 > mouseposx > 1100:
            if 550 > mouseposy > 420:
                if mouseclick == True:
                    self.selectcomponent(3)
                else:
                    self.componentcolour(3,1)
            else:
               self.componentcolour(3,0)
        else:
            self.componentcolour(3,0)
            
    #   When the Mouse is at the resistor
        if 1315 > mouseposx > 1100:
            if 350 > mouseposy > 220:
                if mouseclick == True:
                    self.selectcomponent(2)
                else:
                    self.componentcolour(2,1)
            else:
                self.componentcolour(2,0)
        else:
            self.componentcolour(2,0)
            
    #   When the Mouse is at the power supply
        if 1315 > mouseposx > 1100:
            if 165 > mouseposy > 20:
                if mouseclick == True:
                    self.selectcomponent(1)
                else:
                    self.componentcolour(1,1)
            else:
                self.componentcolour(1,0)
        else:
            self.componentcolour(1,0)
            
    #   When the mouse is at the next button
        if 700 < mouseposx < 766:
            if 10 < mouseposy < 40:
                if mouseclick == True:
                    # creates another instance or
                    #selects a previously created instance with a circular queue method
                    if circuitnumber == 4:
                        circuitnumber = 0
                    else:
                        circuitnumber += 1
                        if circuitsleft[circuitnumber] == 1:
                            circuitsleft[circuitnumber] = 0
                            createcircuit()
                            
                self.write("Next",grey,700,10)
                
    #   When the mouse is at the prev button
        if 590 < mouseposx < 685:
            if 10 < mouseposy < 40:
                if mouseclick == True:
                    # Goes to the previous circuit the user created
                    if circuitnumber == 0:
                        circuitnumber = 4
                    else:
                        circuitnumber -= 1
                self.write("Previous",grey,590,10)
                
    #   When the mouse is at the save button
        if 100 < mouseposx < 166:
            if 10 < mouseposy < 40:
                if mouseclick == True:
                    # saves instance
                    self.save()
                self.write("Save",grey,100,10)
                
    #   When the mouse is at the load button
        if 0 < mouseposx < 66:
            if 10 < mouseposy < 40:
                if mouseclick == True:
                    # Loads a circuit
                    self.load()
                self.write("Load",grey,10,10)
                
    #   When the mouse is at the left series wire
        if 225 > mouseposx > 180:
            if 455 > mouseposy > 150:
                if mouseclick == True:
                    self.addcomponent('Left Series')
                else:
                    pygame.draw.rect(screen, grey, (200,150,3,300),3)
                    self.write('Left Series Wire',black,825,275)
                    self.write(("Resistance "+str("{0:.2f}".format(self.Variables[0][4]))+" Ohms"),black,825,325)
                    self.write(("Current       "+str("{0:.2f}".format(self.Variables[0][2]))+" Amps"),black,825,375)
                    self.write(("Power         "+str("{0:.2f}".format(self.lspower))+" Watts"),black,825,425)
                    self.write(("Voltage       "+str("{0:.2f}".format(self.leftvoltage))+" Volts"),black,825,475)
                    
    #   When the mouse is at the bottom series wire
        if 600 > mouseposx > 197:
            if 475 > mouseposy > 410:
                if mouseclick == True:
                    self.addcomponent('Bottom Series')
                else:
                    pygame.draw.rect(screen, grey, (200,450,400,3),3)
                    self.write('Bottom Series Wire',black,825,275)
                    self.write(("Resistance "+str("{0:.2f}".format(self.Variables[3][4]))+" Ohms"),black,825,325)
                    self.write(("Current       "+str("{0:.2f}".format(self.Variables[3][2]))+" Amps"),black,825,375)
                    self.write(("Power         "+str("{0:.2f}".format(self.bspower))+" Watts"),black,825,425)
                    self.write(("Voltage       "+str("{0:.2f}".format(self.bottomvoltage))+" Volts"),black,825,475)
                    
    #   When the mouse is at the right series wire
        if 630 > mouseposx > 560:
            if 453 > mouseposy > 150:
                if mouseclick == True:
                    self.addcomponent('Right Series')
                else:
                    pygame.draw.rect(screen, grey, (600,150,3,300),3)
                    self.write('Right Series Wire',black,825,275)
                    self.write(("Resistance "+str("{0:.2f}".format(self.Variables[1][4]))+" Ohms"),black,825,325)
                    self.write(("Current       "+str("{0:.2f}".format(self.Variables[1][2]))+" Amps"),black,825,375)
                    self.write(("Power         "+str("{0:.2f}".format(self.rspower))+" Watts"),black,825,425)
                    self.write(("Voltage       "+str("{0:.2f}".format(self.rightvoltage))+" Volts"),black,825,475)
                    
    #   When the mouse is at the top series wire
        if 600 > mouseposx > 197:
            if 185 > mouseposy > 120:
                if mouseclick == True:
                    self.addcomponent('Top Series')
                else:
                    pygame.draw.rect(screen, grey, (200,150,400,3),3)
                    self.write('Top Series Wire',black,825,275)
                    self.write(("Resistance "+str("{0:.2f}".format(self.Variables[2][4]))+" Ohms"),black,825,325)
                    self.write(("Current       "+str("{0:.2f}".format(self.Variables[2][2]))+" Amps"),black,825,375)
                    self.write(("Power         "+str("{0:.2f}".format(self.tspower))+" Watts"),black,825,425)
                    self.write(("Voltage       "+str("{0:.2f}".format(self.topvoltage))+" Volts"),black,825,475)
                    
    #   When the Mouse is at the left parallel circuit
        if 180 > mouseposx > 10:
            if 455 > mouseposy > 150:
                if mouseclick == True:
                    self.addcomponent('Left Parallel')
                else:
                    pygame.draw.rect(screen, grey, (100,150,3,300),3)
                    pygame.draw.rect(screen, grey, (100,150,100,3),3)
                    pygame.draw.rect(screen, grey, (100,450,100,3),3)
                    self.write('Parallel',grey,340,0)
                    self.write('Parallel',grey,340,570)
                    self.write('Left Parallel Wire',black,825,275)
                    self.write(("Resistance "+str("{0:.2f}".format(self.Variables[0][5]))+" Ohms"),black,825,325)
                    self.write(("Current       "+str("{0:.2f}".format(self.Variables[0][3]))+" Amps"),black,825,375)
                    self.write(("Power         "+str("{0:.2f}".format(self.lppower))+" Watts"),black,825,425)
                    self.write(("Voltage       "+str("{0:.2f}".format(self.leftvoltage))+" Volts"),black,825,475)
                    
    #   When the Mouse is at the top parallel circuit
        if 600 > mouseposx > 197:
            if 120 > mouseposy > 20:
                if mouseclick == True:
                    self.addcomponent('Top Parallel')
                else:
                    pygame.draw.rect(screen, grey, (200,75,400,3),3)
                    pygame.draw.rect(screen, grey, (200,75,3,75),3)
                    pygame.draw.rect(screen, grey, (600,75,3,75),3)
                    self.write('Parallel',grey,340,0)
                    self.write('Parallel',grey,340,570)
                    self.write('Top Parallel Wire',black,825,275)
                    self.write(("Resistance "+str("{0:.2f}".format(self.Variables[2][5]))+" Ohms"),black,825,325)
                    self.write(("Current       "+str("{0:.2f}".format(self.Variables[2][3]))+" Amps"),black,825,375)
                    self.write(("Power         "+str("{0:.2f}".format(self.tppower))+" Watts"),black,825,425)
                    self.write(("Voltage       "+str("{0:.2f}".format(self.topvoltage))+" Volts"),black,825,475)
                    
    #   When the Mouse is at the bottom parallel circuit
        if 600 > mouseposx > 197:
            if 575 > mouseposy > 475:
                if mouseclick == True:
                    self.addcomponent('Bottom Parallel')
                else:
                    pygame.draw.rect(screen, grey, (200,525,400,3),3)
                    pygame.draw.rect(screen, grey, (200,455,3,75),3)
                    pygame.draw.rect(screen, grey, (600,455,3,75),3)
                    self.write('Parallel',grey,340,0)
                    self.write('Parallel',grey,340,570)
                    self.write('Bottom Parallel Wire',black,825,275)
                    self.write(("Resistance "+str("{0:.2f}".format(self.Variables[3][5]))+" Ohms"),black,825,325)
                    self.write(("Current       "+str("{0:.2f}".format(self.Variables[3][3]))+" Amps"),black,825,375)
                    self.write(("Power         "+str("{0:.2f}".format(self.bppower))+" Watts"),black,825,425)
                    self.write(("Voltage       "+str("{0:.2f}".format(self.bottomvoltage))+" Volts"),black,825,475)

    #   When the Mouse is at the right parallel circuit
        if 800 > mouseposx > 630:
            if 453 > mouseposy > 150:
                if mouseclick == True:
                    self.addcomponent('Right Parallel')
                else:
                    pygame.draw.rect(screen, grey, (700,150,3,300),3)
                    pygame.draw.rect(screen, grey, (600,150,100,3),3)
                    pygame.draw.rect(screen, grey, (600,450,100,3),3)
                    self.write('Parallel',grey,340,0)
                    self.write('Parallel',grey,340,570)
                    self.write('Right Parallel Wire',black,825,275)
                    self.write(("Resistance "+str("{0:.2f}".format(self.Variables[1][5]))+" Ohms"),black,825,325)
                    self.write(("Current       "+str("{0:.2f}".format(self.Variables[1][3]))+" Amps"),black,825,375)
                    self.write(("Power         "+str("{0:.2f}".format(self.rppower))+" Watts"),black,825,425)
                    self.write(("Voltage       "+str("{0:.2f}".format(self.rightvoltage))+" Volts"),black,825,475)

#---------------------------------------------------------------------------#
                    
    # controls the bulb e.g when it appears and how bright and when
    # the bulb has blown because of too many watts
    # this is repeated for every part of the ciruit that the
    # bulb can be placed
    def bulb(self):
        if self.Variables[0][6]%2 == 1:
            if self.lspower < 70:
                pygame.draw.circle(screen, (255,255,(255-(self.lspower*3.5))), [200, 373], 35)
            else:
                self.msg("More than 70 watts has been passed through the bulb, the bulb has blown")
                self.Variables[0][6] = 0
            self.displayimage("gridvbulbimage.gif",159,325)
        if self.Variables[0][7]%2 == 1:
            if self.Variables[0][5] > 0:
                if self.lppower < (70):
                    pygame.draw.circle(screen, (255,255,255-self.lppower*3.5), [100, 373], 35)
                else:
                    self.msg("More than 70 watts has been passed through the bulb, the bulb has blown")
                    self.Variables[0][7] = 0
                self.displayimage("gridvbulbimage.gif",59,325)
        if self.Variables[1][6]%2 == 1:
            if self.rspower < (70):
                pygame.draw.circle(screen, (255,255,255-self.rspower*3.5), [601, 373], 35)
            else:
                self.msg("More than 70 watts has been passed through the bulb, the bulb has blown")
                self.Variables[1][6] = 0
            self.displayimage("gridvbulbimage.gif",560,325)
        if self.Variables[1][7]%2 == 1:
            if self.Variables[1][5] > 0:
                if self.rppower < (70):
                    pygame.draw.circle(screen, (255,255,255-self.rppower*3.5), [701, 373], 35)
                else:
                    self.msg("More than 70 watts has been passed through the bulb, the bulb has blown")
                    self.Variables[1][7] = 0
                self.displayimage("gridvbulbimage.gif",660,325)
        if self.Variables[2][6]%2 == 1:
            if self.tspower < (70):
                pygame.draw.circle(screen, (255,255,255-self.tspower*3.5), [525, 151], 35)
            else:
                self.msg("More than 70 watts has been passed through the bulb, the bulb has blown")
                self.Variables[2][6] = 0
            self.displayimage("gridhbulbimage.gif",475,115)
        if self.Variables[2][7]%2 == 1:
            if self.Variables[2][5] > 0:
                if self.tppower < (70):
                    pygame.draw.circle(screen, (255,255,255-self.tppower*3.5), [540, 76], 35)
                else:
                    self.msg("More than 70 watts has been passed through the bulb, the bulb has blown")
                    self.Variables[2][7] = 0
                self.displayimage("gridhbulbimage.gif",490,40)
        if self.Variables[3][6]%2 == 1:
            if self.bspower < (70):
                pygame.draw.circle(screen, (255,255,255-self.bspower*3.5), [525, 451], 35)
            else:
                self.msg("More than 70 watts has been passed through the bulb, the bulb has blown")
                self.Variables[3][6] = 0
            self.displayimage("gridhbulbimage.gif",475,415)
        if self.Variables[3][7]%2 == 1:
            if self.Variables[3][5] > 0:
                if self.bppower < (70):
                    pygame.draw.circle(screen, (255,255,255-self.bppower*3.5), [540, 526], 35)
                else:
                    self.msg("More than 70 watts has been passed through the bulb, the bulb has blown")
                    self.Variables[3][7] = 0
                self.displayimage("gridhbulbimage.gif",490,490)

#---------------------------------------------------------------------------#
                
    #   contorls when to display the powersupplies
        if self.Variables[0][8] > 0:
            self.displayimage("gridvdpowersupplyimage.png",166,170)
        if self.Variables[1][8] > 0:
            self.displayimage("gridvupowersupplyimage.png",562,170)
        if self.Variables[2][8] > 0:
            self.displayimage("gridhlpowersupplyimage.png",220,119)
        if self.Variables[3][8] > 0:
            self.displayimage("gridhrpowersupplyimage.png",220,412)
    #   controls when to display the resistors
        if self.Variables[0][4] > 1:
            self.displayimage("gridvresistorimage.png",173,225)
        if self.Variables[1][4] > 1:
            self.displayimage("gridvresistorimage.png",573,225)
        if self.Variables[3][4] > 1:
            self.displayimage("gridhresistorimage.png",362,427)
        if self.Variables[2][4] > 1:
            self.displayimage("gridhresistorimage.png",362,127)

#---------------------------------------------------------------------------#
            
    # creates the grid on screen
    def creategrid(self):
    #   creates parallel wires and decides what colour to make them
        if self.Variables[0][5] == 0:
            pygame.draw.rect(screen, lightgrey, (100,150,3,300),3)
            pygame.draw.rect(screen, lightgrey, (100,150,100,3),3)
            pygame.draw.rect(screen, lightgrey, (100,450,100,3),3)
        else:
            pygame.draw.rect(screen, black, (100,150,3,300),3)
            pygame.draw.rect(screen, black, (100,150,100,3),3)
            pygame.draw.rect(screen, black, (100,450,100,3),3)
            self.displayimage("gridvresistorimage.png", 73,160)
            
        if self.Variables[2][5] == 0:
            pygame.draw.rect(screen, lightgrey, (200,75,400,3),3)
            pygame.draw.rect(screen, lightgrey, (200,75,3,75),3)
            pygame.draw.rect(screen, lightgrey, (600,75,3,75),3)
        else:
            pygame.draw.rect(screen, black, (200,75,400,3),3)
            pygame.draw.rect(screen, black, (200,75,3,75),3)
            pygame.draw.rect(screen, black, (600,75,3,75),3)
            self.displayimage("gridhresistorimage.png", 220,52)
        if self.Variables[1][5] == 0:
            pygame.draw.rect(screen, lightgrey, (700,150,3,300),3)
            pygame.draw.rect(screen, lightgrey, (600,150,100,3),3)
            pygame.draw.rect(screen, lightgrey, (600,450,100,3),3)
        else:

            pygame.draw.rect(screen, black, (600,150,100,3),3)
            pygame.draw.rect(screen, black, (600,450,100,3),3)
            pygame.draw.rect(screen, black, (700,150,3,300),3)
            self.displayimage("gridvresistorimage.png", 673,160)
            
        if self.Variables[3][5] == 0:
            pygame.draw.rect(screen, lightgrey, (200,525,400,3),3)
            pygame.draw.rect(screen, lightgrey, (200,455,3,75),3)
            pygame.draw.rect(screen, lightgrey, (600,455,3,75),3)
        else:
            pygame.draw.rect(screen, black, (200,525,400,3),3)
            pygame.draw.rect(screen, black, (200,455,3,75),3)
            pygame.draw.rect(screen, black, (600,455,3,75),3)
            self.displayimage("gridhresistorimage.png", 220,502)
        
    #   draws series wires onto the screen
        pygame.draw.rect(screen, black, (200,150,3,300),3)
        pygame.draw.rect(screen, black, (600,150,3,300),3)
        pygame.draw.rect(screen, black, (200,150,400,3),3)
        pygame.draw.rect(screen, black, (200,450,400,3),3)
    #   draws lines to separate sections of the screen
        pygame.draw.rect(screen, black, (1100,0,1,600),3)
        pygame.draw.rect(screen, black, (800,0,1,600),3)
        self.bulb()

#---------------------------------------------------------------------------#
        
    # makes the components in the selection area change
    # colour when you hover over them
    def componentcolour(self, comp, colour):        
        if comp == 1:
            if colour == 1:
                self.write("Power Supply",grey,1120,20)
            if colour!= 1:
                self.write("Power Supply",black,1120,20)
        elif comp == 2:
            if colour == 1:
                self.write("Resistor",grey,1120,220)
            if colour!= 1:
                self.write("Resistor",black,1120,220)
        elif comp == 3:
            if colour == 1:
                self.write("Bulb",grey,1120,420)
            if colour!= 1:
                self.write("Bulb",black,1120,420)
        else :
            self.write("Power Supply",black,1120,20)
            self.write("Resistor",black,1120,220)
            self.write("Bulb",black,1120,420)
            
        if self.componentselected == 1 :
            self.write("Power Supply",grey,1120,20)
        elif self.componentselected == 2:
            self.write("Resistor",grey,1120,220)
        elif self.componentselected == 3:
            self.write("Bulb",grey,1120,420)

#---------------------------------------------------------------------------#
            
    # lets the rest of the program know what component you have selected
    def selectcomponent(self, x):
        self.componentselected = x
        if x == 1:
            self.componentcolour(1,1)
            self.msg("Power Supply Selected, click a series wire to add voltage.")   
        elif x == 2:
            self.componentcolour(2,1)
            self.msg("Resistor Selected, click a wire to add resistance.")
        else :
            self.componentcolour(3,1)
            self.msg("70 Watt Bulb Selected, click a wire to add bulb.")

#---------------------------------------------------------------------------#
    # saves all of the variables to a text file 
    def save(self):
        f = open("savefile.txt","w") #opens file called "savefile.txt"
        f.write(str(self.Variables))
    # an algorithm to only read numbers from the text file
    # the algorithm distigusished what is a float number and
    # saves it and discards any anything else that is also
    # saved with the data for example brackts and commas 
    def load(self):
        f = open("savefile.txt","r") #opens file called "savefile.txt"
        mainlist = []
        
        for o in range (0,4):
            sublist = []
            for h in range (0,9):
                n = ""
                p=[]
                l = f.read(1)
                if l == ",":
                    l = f.read(1) 
                while l == " " or l == "" or l == "[":
                    l = f.read(1)
                while l != "," and l != "]":  
                    n = n + l
                    l = f.read(1)
                l = f.read(1)
                if n != "":
                    p.append(float(n))
                    sublist.extend(p)
            mainlist.append(sublist)
        self.Variables = mainlist
        z = ""
        l = f.read(1)
        while l != "]":
            z = z+ l
            l = f.read(1)
        self.Variables.append(float(z))
        self.updateleftwire()
        self.updaterightwire()
        self.updatetopwire()
        self.updatebottomwire()
        self.updatecircuit()

#---------------------------------------------------------------------------#
        
    #changes variables of the wire based on what component is selected
    def addcomponent(self, wire):
        #if a powersupply is added
        if self.componentselected == 1:
            if wire == 'Left Series':
                self.Variables[0][8] = 1
            elif wire == 'Right Series':
                self.Variables[1][8] = 1
            elif wire == 'Top Series':
                self.Variables[2][8] = 1
            elif wire == 'Bottom Series':
                self.Variables[3][8] = 1
            else:
                self.msg("Place Power Supply on a series wire.")
            self.Variables[4]  += 1
            self.updatecircuit()
            
        # if a resistor is added
        if self.componentselected == 2:
            if wire == 'Left Series':
                self.Variables[0][4] += 1
                self.updateleftwire()
                self.updatecircuit()
            elif wire == 'Left Parallel':
                self.Variables[0][5] += 1
                self.updateleftwire()
                self.updatecircuit()
            if wire == 'Right Series':
                self.Variables[1][4] += 1
                self.updaterightwire()
                self.updatecircuit()
            elif wire == 'Right Parallel':
                self.Variables[1][5] += 1
                self.updaterightwire()
                self.updatecircuit()
            if wire == 'Top Series':
                self.Variables[2][4] += 1
                self.updatetopwire()
                self.updatecircuit()
            elif wire == 'Top Parallel':
                self.Variables[2][5] += 1
                self.updatetopwire()
                self.updatecircuit()
            if wire == 'Bottom Series':
                self.Variables[3][4] += 1
                self.updatebottomwire()
                self.updatecircuit()
            elif wire == 'Bottom Parallel':
                self.Variables[3][5] += 1
                self.updatebottomwire()
                self.updatecircuit()
                
         # if a bulb is added
        if self.componentselected == 3:
            if wire == 'Left Series':
                self.Variables[0][6] += 1
                self.updateleftwire()
                self.updatecircuit()
            elif wire == 'Left Parallel':
                self.Variables[0][7] += 1
                self.updateleftwire()
                self.updatecircuit()
            if wire == 'Right Series':
                self.Variables[1][6] += 1
                self.updaterightwire()
                self.updatecircuit()
            elif wire == 'Right Parallel':
                self.Variables[1][7] += 1
                self.updaterightwire()
                self.updatecircuit()
            if wire == 'Top Series':
                self.Variables[2][6] += 1
                self.updatetopwire()
                self.updatecircuit()
            elif wire == 'Top Parallel':
                self.Variables[2][7] += 1
                self.updatetopwire()
                self.updatecircuit()
            if wire == 'Bottom Series':
                self.Variables[3][6] += 1
                self.updatebottomwire()
                self.updatecircuit()
            elif wire == 'Bottom Parallel':
                self.Variables[3][7] += 1
                self.updatebottomwire()
                self.updatecircuit()
    
#---------------------------------------------------------------------------#

def createcircuit():
    #creates and instance of the class with all of the variables 
    list1[circuitnumber] = wire()

#---------------------------------------------------------------------------#

# Creates two lists and a varible are used in the creation
#  and selection of multiple instances of the circiut
list1=[1,2,3,4,5]
circuitnumber = 0
circuitsleft = [1,1,1,1,1]
createcircuit()

#---------------------------------------------------------------------------#

#defined colours
white = (255,255,255)
grey = (200,200,200)
lightgrey = (245,245,245)
black = (0,0,0)

#---------------------------------------------------------------------------#

#creates font for text
font = pygame.font.SysFont("arial", 30)

#---------------------------------------------------------------------------#

#creates display
screen = pygame.display.set_mode((1320,600))
pygame.display.set_caption('Circuit Simulator')
screen.fill(white)
pygame.display.update()
# these are instructions on how to use the program
list1[circuitnumber].msg("Welcome to the Circuit Simulation, this is an accurate simulation of how a circuit works!")
list1[circuitnumber].msg("Instructions: To select a component, you click on the picture of it in the section to the right of the screen. To add this component to the circuit, you click on an area of the circuit where you would like to add the selected component. When a bulb and a resistor are placed on the same wire, the resistance acts as internal resistance for bulb. Add resistance to the greyed out wires to add them to the circuit. To increase the effects of a component, place another component of the same type to the same area, the effects  of the first components will be increases by 1.")

#---------------------------------------------------------------------------#

#main program loop
Program = True
while Program == True:

#---------------------------------------------------------------------------#
    
    screen.fill(white)
    list1[circuitnumber].componentcolour(0, 1)

#---------------------------------------------------------------------------#    
    
# Draws buttons and wires on the screen 
    list1[circuitnumber].write('Series Components',black,280,275)
    list1[circuitnumber].write('Parallel',black,340,0)
    list1[circuitnumber].write('Parallel',black,340,570)
    list1[circuitnumber].write('Save',black,100,10)
    list1[circuitnumber].write('Load',black,10,10)
    list1[circuitnumber].write('Next',black,700,10)
    list1[circuitnumber].write('Previous',black,590,10)
    list1[circuitnumber].write('Circuit '+str(circuitnumber+1),black,475,10)
    list1[circuitnumber].displayimage("bulbimage.png",1120,470)
    list1[circuitnumber].displayimage("resistorimage.png",1120,270)
    list1[circuitnumber].displayimage("powersupplyimage.png",1120,80)
    list1[circuitnumber].write("Circuit Variables",black,825,0)
    list1[circuitnumber].write(str("{0:.2f}".format(list1[circuitnumber].Variables[4]))+" Volts",black,825,50)
    list1[circuitnumber].write(str("{0:.2f}".format(list1[circuitnumber].resistance))+" Ohms",black,825,100)
    list1[circuitnumber].write(str("{0:.2f}".format(list1[circuitnumber].current))+" Amps",black,825,150)
    list1[circuitnumber].write(str("{0:.2f}".format(list1[circuitnumber].power))+" Watts",black,825,200)
    
#---------------------------------------------------------------------------#
    
# Makes program interactive with the mouse
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            list1[circuitnumber].mousefunction(mousepos[0], mousepos[1], True)
        pass
    
#---------------------------------------------------------------------------#
    # this stops the program trying to access an instance of the circuit that
    # does not yet exist
    while True:
        try:
            list1[circuitnumber].creategrid()
            break
        except:
            circuitnumber -= 1

#---------------------------------------------------------------------------#
            
    list1[circuitnumber].mousefunction(mousepos[0], mousepos[1], False)

#---------------------------------------------------------------------------#
    
    #   closes the program
    if event.type == pygame.QUIT:
        Program = False

#---------------------------------------------------------------------------#
        
    pygame.display.update()
pygame.quit()
