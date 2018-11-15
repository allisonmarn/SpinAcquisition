import thorlabs_apt as apt
import time
__cntrl_x = None
__cntrl_y = None
__cntrl_z = None

def __initialize_stages():
    global __cntrl_x
    global __cntrl_y
    global __cntrl_z

    # get current device lists
    devices = apt.list_available_devices()

    # SNs of the KDC101 devices
    x_stage = 27002265
    y_stage = 27002165
    z_stage = 27002158

    # initialize the motor controllers
    __cntrl_x = apt.Motor(x_stage)
    __cntrl_y = apt.Motor(y_stage)
    __cntrl_z = apt.Motor(z_stage)
    print('Stages are initialized...')

    # default positions of x,y, and z all in microns
    x_pos = 5
    y_pos = 5
    z_pos = 5
    
    # homing
    print('Homing is started...')
    __cntrl_x.move_home()
    time.sleep(1)    # pause 5 to homing
    __cntrl_y.move_home()
    time.sleep(1)    # pause 5 to homing
    __cntrl_z.move_home()
    time.sleep(60)    # pause 5 to homing
    print('Homing is finished...')

    # go to home positions

    print('Going to default positions...')
    __cntrl_x.move_to(x_pos)
    time.sleep(1)
    __cntrl_y.move_to(y_pos)
    time.sleep(1)
    __cntrl_z.move_to(z_pos)
    time.sleep(20)    # pause 5 to homing
    print('Stages are ready...')



def __go_y(position):
    global __cntrl_y
    # go to positions
    __cntrl_y.move_by(position*1e-3)


def __go_x(position):
    global __cntrl_x
    # go to positions
    __cntrl_x.move_by(position*1e-3)


def __go_z(position):
    global __cntrl_z
    # go to positions
    __cntrl_z.move_by(position*1e-3)

def __check_objective():
    var = input("Is objective mounted (Y/N): ")
    if (var == 'Y'):
        return True
    else:
        return False

""" 
import thorlabs_apt as apt

__cntrl_x = None
__cntrl_y = None
__cntrl_z = None


def __initialize_stages():
    global __cntrl_x
    global __cntrl_y
    global __cntrl_z




def __go_y(position):
    print(position)

    # go to positions


def __go_x(position):
    print(position)
    # go to positions


def __go_z(position):
    print(position)
    # go to positions
"""
