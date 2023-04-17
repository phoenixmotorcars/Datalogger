import os
import can
import cantools
import lib.CAN_read as CAN_read

def CAN_INIT():
    os.system('sudo ip link set can0 type can bitrate 500000')
    os.system('sudo ifconfig can0 up')

    can_interface = 'socketcan'
    can_channel   = 'can0'
    can_bus       = can.interface.Bus(channel=can_channel, interface=can_interface)
    return can_bus

def read_message(can_bus):
    message = can_bus.recv()
    return message