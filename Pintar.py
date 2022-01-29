from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations
RDK = Robolink()

#poner Ur10 A en home 
robot= RDK.Item('RobotB',ITEM_TYPE_ROBOT)
robot.MoveJ(robot.JointsHome())

t1= RDK.Item('Face_U', ITEM_TYPE_TARGET) 
t2= RDK.Item('Right_U', ITEM_TYPE_TARGET) 
t3= RDK.Item('Center_D', ITEM_TYPE_TARGET)
t4= RDK.Item('Left_U', ITEM_TYPE_TARGET)
robot.MoveL(t1)

a1=t1.Pose()*transl(-100,0,0)
robot.MoveJ(a1)

#cara lateral
robot.MoveJ(t2)
a2=t2.Pose()*transl(-60,40,0)
robot.MoveJ(a2)
a3=a2*transl(-60,40,0)
robot.MoveJ(a3)
a4=a3*transl(0,0,-50)
robot.MoveJ(a4)

#Cara Superior
robot.MoveJ(t3)
a2=t3.Pose()*transl(-60,40,0)
robot.MoveJ(a2)
a3=a2*transl(-60,40,0)
robot.MoveJ(a3)
a4=a3*transl(0,150,0)
robot.MoveJ(a4)

#cara lateral 2
robot.MoveJ(t4)
a2=t4.Pose()*transl(60,40,0)
robot.MoveJ(a2)
a3=a2*transl(60,40,0)
robot.MoveJ(a3)
a4=a3*transl(0,0,-50)

robot.MoveJ(a4)
robot.MoveJ(robot.JointsHome())