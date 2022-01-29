from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations
RDK = Robolink()

PARAM_SIZE_PALLET = 'SizePallet'                    #numero de cubos
PARAM_COLOR_OBJECT = 'ColorObject' 

#poner Ur10 A en home 
robot= RDK.Item('RobotA',ITEM_TYPE_ROBOT)
tool=  RDK.Item('RobotiQ Sanding Kit', ITEM_TYPE_TOOL)

def TCP_On(toolitem):
    """Attaches the closest object to the toolitem Htool pose,
    It will also output appropriate function calls on the generated robot program (call to TCP_On)"""
    toolitem.AttachClosest()
    toolitem.RDK().RunMessage('Set air valve on')
    toolitem.RDK().RunProgram('TCP_On()');

robot.MoveJ(robot.JointsHome())

t1= RDK.Item('CercaCajas', ITEM_TYPE_TARGET) 
t2= RDK.Item('1erCubo', ITEM_TYPE_TARGET)                                                              #CAMBIA

t3= RDK.Item('Cerca Paint', ITEM_TYPE_TARGET) 
t4= RDK.Item('MesaPint', ITEM_TYPE_TARGET) 

t5= RDK.Item('CercaDejarCajas', ITEM_TYPE_TARGET) 
t6= RDK.Item('1erCuboDejar', ITEM_TYPE_TARGET)                                                         #CAMBIA

a=RDK.getParam(PARAM_SIZE_PALLET)
b=0
while (a>0):
    #MOVIMIENTOS 
    robot.MoveJ(t1)                     # move to aproach

    a2=t2.Pose()*transl(150*b,-16*b,0)

    robot.MoveJ(a2)

    TCP_On(tool)
    robot.MoveJ(t1)                     # move to aproach
    robot.MoveJ(t3)                     # move to aproach table paint
    robot.MoveJ(t4)                     # put in table 
    tool.DetachAll()
    robot.MoveJ(t3)                     # move to aproach table paint

    RDK.RunProgram("pint", wait_for_finished=True)

    
    #repintar
    #COLORES 1. Red \n2. Green \n3. Blue \n4. Pink'
    coloresL=[[1,0,0],[0,1,0],[0,0,1],[1,0,1]]
    objecta='Part '+str(b+1)
    Cubo = RDK.Item(objecta, ITEM_TYPE_OBJECT)
    cnume=RDK.getParam(PARAM_COLOR_OBJECT)
    cCode=coloresL[int(cnume)-1]
    Cubo.Recolor(cCode)
    #-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
    robot.MoveJ(t4)                     # put in table 
    TCP_On(tool)
    robot.MoveJ(t3)                     # move to aproach table paint
    
    robot.MoveJ(t5)                     # move to aproach table f

    a6=t6.Pose()*transl(150*b,-16*b,0)

    robot.MoveJ(a6)
    tool.DetachAll()
    robot.MoveJ(t5)                      # move to aproach table f                  

    a-=1
    b+=1