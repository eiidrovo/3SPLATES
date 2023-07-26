import numpy as np
import json

# This code was made by ESAU IDROVO (ESPOL -Ecuador)


def mngen (parity, terms):
    numbers=[]
    if parity == "even":
        for i in range(2,2*terms,2):
            numbers.append(i)
    elif parity == "odd":
        for i in range(1,2*terms,2):
            numbers.append(i)
        
    elif parity == "none":
        for i in range(1,terms+1):
            numbers.append(i)
    else:
        return(None)
    mn=np.array(np.meshgrid(numbers, numbers)).T.reshape(-1, 2)
    #Return an array with 2 columns with a combination of all m and n terms
    return(mn)

def platecoords(lenghtx, lenghty, subdititions):
    x =np.linspace(0, lenghtx, subdititions+1)
    y =np.linspace(0, lenghty, subdititions+1)
    xx, yy = np.meshgrid(x, y)
    coordinates = np.column_stack((xx.ravel(), yy.ravel()))
    return (coordinates)

# LOAD DISTRIBUTION #
def load_dist (p, mnterms, platecoords, lenghtx, lenghty):
    pxy= np.zeros(  np.shape(platecoords)[0])
    for xy in enumerate(platecoords):
        for mn in mnterms:
            Pmn = 16*p/(mn[0]*mn[1]*np.pi**2)
            pxy[xy[0]]+= Pmn * np.sin(mn[0]*np.pi*xy[1][0]/lenghtx)* np.sin(mn[1]*np.pi*xy[1][1]/lenghty)
    pxy=np.column_stack((platecoords,pxy))
    #Return an array with 3 columns [x, y, p]
    return(pxy)

def load_point(F, mnterms, platecoords, lenghtx, lenghty,posx,posy):
    pxy= np.zeros(np.shape(platecoords)[0])
    for xy in enumerate(platecoords):
        for mn in mnterms:
            Pmn =(4*F/(lenghtx*lenghty))*(np.sin(mn[0]*np.pi*posx/lenghtx))*(np.sin(mn[1]*np.pi*posy/lenghty))
            pxy[xy[0]]+= Pmn* np.sin(mn[0]*np.pi*xy[1][0]/lenghtx)* np.sin(mn[1]*np.pi*xy[1][1]/lenghty)
    pxy=np.column_stack((platecoords,pxy))
    return(pxy)

#DEFLECTION

def deflect_dist (p, mnterms, platecoords, lenghtx, lenghty):
    wxy= np.zeros(np.shape(platecoords)[0])
    for xy in enumerate(platecoords):
        for mn in mnterms:    
            Pmn=16*p/(mn[0]*mn[1]*np.pi**2)
            Wmn = Pmn / (D * np.pi**4 * ((mn[0]/lenghtx)**2+(mn[1]/lenghty)**2)**2)
            wxy[xy[0]] += Wmn *  np.sin(mn[0]*np.pi*xy[1][0]/lenghtx)* np.sin(mn[1]*np.pi*xy[1][1]/lenghty)
    wxy=np.column_stack((platecoords,wxy))

    #Return an array with 3 columns [x, y, w]
    return(wxy)

def deflect_point (F, mnterms, platecoords, lenghtx, lenghty,posx,posy):
    wxy= np.zeros(np.shape(platecoords)[0])
    for xy in enumerate(platecoords):
        for mn in mnterms:
            Pmn =(4*F/(lenghtx*lenghty))*(np.sin(mn[0]*np.pi*posx/lenghtx))*(np.sin(mn[1]*np.pi*posy/lenghty))
            Wmn = Pmn / (D * np.pi**4 * ((mn[0]/lenghtx)**2+(mn[1]/lenghty)**2)**2)
            wxy[xy[0]]+= Wmn* np.sin(mn[0]*np.pi*xy[1][0]/lenghtx)* np.sin(mn[1]*np.pi*xy[1][1]/lenghty)
    wxy=np.column_stack((platecoords,wxy))
    #Return an array with 3 columns [x, y, w]
    return(wxy)

#Moments
#dist

def momentx_dist(p, mnterms, platecoords, lenghtx, lenghty):
    Mx= np.zeros(np.shape(platecoords)[0])
    for xy in enumerate(platecoords):
        for mn in mnterms:
            Pmn=16*p/(mn[0]*mn[1]*np.pi**2)
            Wmn = Pmn / (D * np.pi**4 * ((mn[0]/lenghtx)**2+(mn[1]/lenghty)**2)**2)
            Mx[xy[0]]+= Wmn * ((mn[0]*np.pi**2/lenghtx)+pois*(mn[1]*np.pi/lenghty)**2) * np.sin(mn[0]*np.pi*xy[1][0]/lenghtx)* np.sin(mn[1]*np.pi*xy[1][1]/lenghty)
    Mx = D * Mx
    Mx=np.column_stack((platecoords,Mx))
    #Return an array with 3 columns [x, y, Mx]
    return(Mx)

def momenty_dist(p, mnterms, platecoords, lenghtx, lenghty):
    My= np.zeros(np.shape(platecoords)[0])
    for xy in enumerate(platecoords):
        for mn in mnterms:
            Pmn=16*p/(mn[0]*mn[1]*np.pi**2)
            Wmn = Pmn / (D * np.pi**4 * ((mn[0]/lenghtx)**2+(mn[1]/lenghty)**2)**2)
            My[xy[0]]+= Wmn * ((mn[1]*np.pi**2/lenghtx)+pois*(mn[0]*np.pi/lenghty)**2) * np.sin(mn[0]*np.pi*xy[1][0]/lenghtx)* np.sin(mn[1]*np.pi*xy[1][1]/lenghty)
    My = D * My
    My=np.column_stack((platecoords,My))
    #Returns an array with 3 columns [x, y, My]
    return(My)

#point
def momentx_point(F, mnterms, platecoords, lenghtx, lenghty,posx,posy):
    Mx= np.zeros(np.shape(platecoords)[0])
    for xy in enumerate(platecoords):
        for mn in mnterms:
            Pmn=(4*F/(lenghtx*lenghty))*(np.sin(mn[0]*np.pi*posx/lenghtx))*(np.sin(mn[1]*np.pi*posy/lenghty))
            Wmn = Pmn / (D * np.pi**4 * ((mn[0]/lenghtx)**2+(mn[1]/lenghty)**2)**2)
            Mx[xy[0]]+= Wmn * ((mn[0]*np.pi**2/lenghtx)+pois*(mn[1]*np.pi/lenghty)**2) * np.sin(mn[0]*np.pi*xy[1][0]/lenghtx)* np.sin(mn[1]*np.pi*xy[1][1]/lenghty)
    Mx = D * Mx
    Mx=np.column_stack((platecoords,Mx))
    #Returns an array with 3 columns [x, y, Mx]
    return(Mx)

def momenty_point(F, mnterms, platecoords, lenghtx, lenghty,posx,posy):
    My= np.zeros(np.shape(platecoords)[0])
    for xy in enumerate(platecoords):
        for mn in mnterms:
            Pmn=(4*F/(lenghtx*lenghty))*(np.sin(mn[0]*np.pi*posx/lenghtx))*(np.sin(mn[1]*np.pi*posy/lenghty))
            Wmn = Pmn / (D * np.pi**4 * ((mn[0]/lenghtx)**2+(mn[1]/lenghty)**2)**2)
            My[xy[0]]+= Wmn * ((mn[1]*np.pi**2/lenghtx)+pois*(mn[0]*np.pi/lenghty)**2) * np.sin(mn[0]*np.pi*xy[1][0]/lenghtx)* np.sin(mn[1]*np.pi*xy[1][1]/lenghty)
    My = D * My
    My=np.column_stack((platecoords,My))
    #Returns an array with 3 columns [x, y, My]
    return(My)

#Normal stresses


def normalstresx(factor, momentx):
    momentx[:,2] *= factor
    sigmax = momentx
    #Return an array with 3 columns [x, y, sigmax]
    return(sigmax)

def normalstresy(factor, momenty):
    momenty[:,2] *= factor
    sigmay = momenty
    #Return an array with 3 columns [x, y, sigmay]
    return(sigmay)



# IMPORT DATA
data = json.load(open('plate.json'))
E = data["E"]
Yield = data["yield"]
pois = data["pois"]
lenghtx = data ["lenghtx"]
lenghty = data ["lenghty"]
thickness = data ["thickness"]
z=data ["z"]
F = data["F"]
XF = data["XF"]
YF = data["YF"]
resolution = data["Resolution"]
parity = data["parity"]
terms = data["terms"]
typeofforce= data["type"]
#Flexural Rigidity
D = E*thickness**3/(12*(1-pois**2))
#Factor for normal stress
factor= 12*z/thickness**3

mn=mngen(parity, terms)


coords=platecoords(lenghtx,lenghty,resolution)

if typeofforce == "distributed":
    load = load_dist(F, mn, coords, lenghtx,lenghty)
    deflection= deflect_dist(F, mn, coords,lenghtx, lenghty)
    momentx = momentx_dist(F, mn, coords, lenghtx, lenghty)
    momenty = momenty_dist(F, mn, coords, lenghtx, lenghty)
    sigmax = normalstresx(factor, momentx)
    sigmay = normalstresx(factor, momenty)

    # With this values you can check if the plate satisfies the allowable values or not making an if or something extra

    maxdefl = np.max(np.abs(deflection[:,2]))
    maxsigmax = np.max(np.abs(sigmax[:,2]))
    maxsigmay = np.max(np.abs(sigmay[:,2]))


    ## this array contains the results x, y, pxy, mx, my, sigmx, sigmy in this order.
    outputarray = np.column_stack((coords,load[:,2], momentx[:,2],momenty[:,2],sigmax[:,2], sigmay[:,2]))

    np.savetxt('output.log',
            outputarray,
            newline='\n',
            delimiter=',',
            header='''

    Output.
    EIIS (2023)- ESPOL
    https://github.com/eiidrovo/3SPLATES    
    Max deflection [m] = {}
    Max stress in x [N/m2] = {}
    Max stress in y [N/m2] = {}
   
    x[m]    y[m]    P[N/m2]     Mx[N]       My[N]       Sigma x[N/m2]        Sigma y [Nm/m2] \n
    

    '''.format(maxdefl, maxsigmax, maxsigmay))   


elif typeofforce == "point":
    load = load_point(F, mn, coords, lenghtx,lenghty, XF, YF)
    deflection= deflect_point(F, mn, coords, lenghtx,lenghty, XF, YF)
    momentx = momentx_point(F, mn, coords, lenghtx,lenghty, XF, YF)
    momenty = momenty_point(F, mn, coords, lenghtx,lenghty, XF, YF)
    sigmax = normalstresx(factor, momentx)
    sigmay = normalstresx(factor, momenty)

    # With this values you can check if the plate satisfies the allowable values or not making an if or something extra
    maxdefl = np.max(np.abs(deflection[:,2]))
    maxsigmax = np.max(np.abs(sigmax[:,2]))
    maxsigmay = np.max(np.abs(sigmay[:,2]))

    
    ## this array contains the results x, y, pxy, mx, my, sigmx, sigmy
    outputarray = np.column_stack((coords,load[:,2], momentx[:,2],momenty[:,2],sigmax[:,2], sigmay[:,2]))

    np.savetxt('output.log',
            outputarray,
            newline='\n',
            delimiter=',',
            header='''

    Output.
    EIIS (2023)- ESPOL
    https://github.com/eiidrovo/3SPLATES    
    Max deflection [m] = {}
    Max stress in x [N/m2] = {}
    Max stress in y [N/m2] = {}
   
    x[m]    y[m]    P[N/m2]     Mx[N]       My[N]       Sigma x[N/m2]        Sigma y [Nm/m2] \n
    

    '''.format(maxdefl, maxsigmax, maxsigmay))   


else:
    print("Cannot being calculated anything, review your spelling in the plate.json file")
    exit()

