from selenium import *
import subprocess
import os
from sys import platform
import threading
import signal

class SeleniumServer(threading.Thread):
    out_file = None

    def run(self, log_file="./out.txt"):
        self.out_file = open(log_file, mode='a')
        self.current_process = self.__get_subprocess_for_os(self.out_file)

    def __get_subprocess_for_os(self,log_file):
        serverJar = os.path.dirname(__file__) + "/lib/selenium-server/selenium-server.jar"

        if platform == 'win32': 
            return subprocess.Popen("java -jar %s" %(serverJar), stdout=log_file)
        else:
            return subprocess.Popen("java -jar %s" %(serverJar), stdout=self.out_file, shell=True)

    def stop(self):
        self.out_file.close()
        if platform == 'win32': 
            import ctypes
            ctypes.windll.kernel32.TerminateProcess(int(self.current_process._handle), -1)
        else:
            os.kill(os.getpid(), signal.SIGKILL)
