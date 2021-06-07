import sys
from data.data import *


def help():
    print("--init : 주식 데이터를 세팅합니다.")



if __name__ == "__main__":
    
    if len(sys.argv) < 2 :
        help()
    
    elif sys.argv[1] == "--init":
        init_data()