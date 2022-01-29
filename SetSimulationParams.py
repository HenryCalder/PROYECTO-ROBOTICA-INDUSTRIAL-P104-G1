# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Note: you do not need to keep a copy of this file, your python script is saved with the station
from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations


PARAM_SIZE_BOX = 'SizeBox'
PARAM_SIZE_PALLET = 'SizePallet'
PARAM_CONV_SPEED_MM = 'ConvSpeed'
PARAM_COLOR_OBJECT = 'ColorObject' 


RDK = Robolink()

size_box = RDK.getParam(PARAM_SIZE_BOX)
size_pallet = RDK.getParam(PARAM_SIZE_PALLET)
conv_speed = RDK.getParam(PARAM_CONV_SPEED_MM)


'''
# ------------------------------------------------------------
size_box_input = mbox('Ingrese el tamaño del objeto en mm [L,W,H]', entry=size_box)
if size_box_input:
    RDK.setParam(PARAM_SIZE_BOX, size_box_input)
else:
    raise Exception('Operacion cancelada por el usuario')
'''


# ------------------------------------------------------------
size_pallet_input = mbox('Ingrese el numero de objetos que desea pintar (min2-max5)', entry='3')
if size_pallet_input:
    RDK.setParam(PARAM_SIZE_PALLET, str(size_pallet_input))
else:
    raise Exception('Operacion cancelada por el usuario')

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
color_object_input = mbox('Elija el numero de acuerdo al color que desea pintar el objeto: \n1. Red \n2. Green \n3. Blue \n4. Pink', entry='1')
if color_object_input:
    RDK.setParam(PARAM_COLOR_OBJECT, color_object_input)
else:
    raise Exception('Operacion cancelada por el usuario')


'''
# ------------------------------------------------------------
conv_speed_input = mbox('Ingrese la velocidad de la banda en mm/s', entry=conv_speed)
if conv_speed_input:
    RDK.setParam(PARAM_CONV_SPEED_MM, conv_speed_input)
    conv_speed = float(conv_speed_input)
    conv = RDK.Item('Conveyor Belt', ITEM_TYPE_ROBOT)
    conv.setSpeed(conv_speed)
    
else:
    raise Exception('Operation cancelled by user')

'''

