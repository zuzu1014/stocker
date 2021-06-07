

import time
import datetime
import inspect
import functools
import traceback
import inspect
import os
import sys

from threading import Thread
from itertools import cycle


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    TIME = '\033[92m'
    MAGNETA = '\033[32m'




class Tracker:
    
    def __init__(self):
        self.tasks = None
        self.fail = False
        self.errors = None
        self.whence = inspect.stack()[1][3].upper()

        

        
        
    def __enter__(self):
        return self




    def __exit__(self, exc_type, exc_value, tb):
        pass



    def append_tasks(self, *tasks):
        self.tasks = []
        for task in tasks:
            self.tasks.append(task)



    def start(self):
        
        print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}------------------------------------------------------------",)
        print(f"  {self.whence} START! ")
        print(f"-----------------------------------------------------------\n",)
        self.start_time = time.time()
        self._track()



    def t_print(self, text, color="\033[97m", *option):
        now = datetime.datetime.now()
        current_time = f" [{now.hour}:{now.minute}:{now.second}] "
        print(f"{bcolors.TIME}{current_time}{bcolors.ENDC}{color}{text}{bcolors.ENDC}")




    def _track(self):
  

        while self.tasks:
            
            try:   
                task = self.tasks.pop(0)
                print(f"{bcolors.HEADER}{bcolors.BOLD} NOW PROCESSING {bcolors.WARNING}{task.__name__}{bcolors.HEADER} IT WILL TAKE SOME TIME{bcolors.ENDC}")
                sys.stdout.write("\033[F") #back to previous line
                sys.stdout.write("\033[K") #clear line
                task()
                self.t_print(f"{task.__name__}{bcolors.OKCYAN}{bcolors.BOLD} COMPLETE {bcolors.ENDC}{bcolors.ENDC}", "\033[97m")
                
                time.sleep(0.1)
                
                
            except Exception as e:
                self.t_print(f"{task.__name__}{bcolors.FAIL}{bcolors.BOLD} FAIL{bcolors.ENDC}{bcolors.ENDC}", "\033[97m")
                self.tasks = None
                self.fail = True
                self.errors = traceback.format_exc()
                break
            
        
        self.stop()



    def stop(self):
        
        run_time = (time.time() - self.start_time).__format__(".2f")
        
        
        if self.fail:
            
            self.t_print("========================================================================\n", bcolors.WARNING)
            print(self.errors)
            self.t_print("========================================================================", bcolors.WARNING)
            self.t_print(f"\r{bcolors.FAIL}{bcolors.BOLD}Error occured!{bcolors.ENDC}{bcolors.ENDC}")
            
            return
        
        
        print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}------------------------------------------------------------{bcolors.ENDC}")
        self.t_print(f"{bcolors.OKBLUE}{bcolors.BOLD}Completed successfully!{bcolors.ENDC}{bcolors.ENDC} Done in {bcolors.WARNING}{run_time}{bcolors.ENDC} seconds.")
        print(f"{bcolors.OKCYAN}{bcolors.BOLD}------------------------------------------------------------{bcolors.ENDC}\n")

              

