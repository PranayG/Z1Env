import os


def getDataPath():
    resdir = os.path.join(os.path.dirname(__file__))
    return resdir


from Z1Env.z1_env import Z1Sim
from Z1Env.gripper_env import GripperSim
