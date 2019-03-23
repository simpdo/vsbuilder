import os
import uuid

from solution import *

def checkProjectDir():
    os.getcwd()




if __name__ == "__main__":
    solution = VsSolution()
    solution.add_project("hall", uuid.uuid4())
    solution.add_project("hall2", uuid.uuid4())
    solution.add_project("hall3", uuid.uuid4())
    solution.save2file()