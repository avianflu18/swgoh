# -*- encoding=utf8 -*-
__author__ = "DarthYu"
import sys
from airtest.core.api import *

def main():
    while 1:
        if exists(Template(r"tpl1605992707698.png", record_pos=(0.0, -0.003), resolution=(1280, 720))):
            sys.exit()
        elif exists(Template(r"tpl1605937955537.png", record_pos=(0.17, 0.243), resolution=(1280, 720))):
            wait(Template(r"tpl1605937955537.png", record_pos=(0.17, 0.243), resolution=(1280, 720)),intervalfunc=main)
            touch(Template(r"tpl1605937955537.png", record_pos=(0.17, 0.243), resolution=(1280, 720)))
            wait(Template(r"tpl1605938079807.png", record_pos=(0.382, 0.242), resolution=(1280, 720)),intervalfunc=main)
            touch(Template(r"tpl1605938079807.png", record_pos=(0.382, 0.242), resolution=(1280, 720))) 
        elif exists(Template(r"tpl1605938079807.png", record_pos=(0.382, 0.242), resolution=(1280, 720))):
            wait(Template(r"tpl1605938079807.png", record_pos=(0.382, 0.242), resolution=(1280, 720)),intervalfunc=main)
            touch(Template(r"tpl1605938079807.png", record_pos=(0.382, 0.242), resolution=(1280, 720)))
        elif exists(Template(r"tpl1605938171486.png", record_pos=(0.384, 0.243), resolution=(1280, 720))):
            wait(Template(r"tpl1605938171486.png", record_pos=(0.384, 0.243), resolution=(1280, 720)),intervalfunc=main)
            touch(Template(r"tpl1605938171486.png", record_pos=(0.384, 0.243), resolution=(1280, 720)))
        elif exists(Template(r"tpl1605943853149.png", record_pos=(0.362, 0.232), resolution=(1280, 720))):
            wait(Template(r"tpl1605943853149.png", record_pos=(0.362, 0.232), resolution=(1280, 720)),intervalfunc=main)
            touch(Template(r"tpl1605943853149.png", record_pos=(0.362, 0.232), resolution=(1280, 720)))

        else:
            if exists(Template(r"tpl1605943770685.png", record_pos=(0.081, -0.134), resolution=(1280, 720))):
                wait(Template(r"tpl1605943770685.png", record_pos=(0.081, -0.134), resolution=(1280, 720)),intervalfunc=main)
                touch(Template(r"tpl1605943770685.png", record_pos=(0.081, -0.134), resolution=(1280, 720)))
            elif exists(Template(r"tpl1605989298314.png", record_pos=(0.071, -0.136), resolution=(1280, 720))):
                wait(Template(r"tpl1605989298314.png", record_pos=(0.071, -0.136), resolution=(1280, 720)),intervalfunc=main)
                touch(Template(r"tpl1605989298314.png", record_pos=(0.071, -0.136), resolution=(1280, 720)))
            elif exists(Template(r"tpl1605989397146.png", record_pos=(-0.362, 0.083), resolution=(1280, 720))):
                wait(Template(r"tpl1605989397146.png", record_pos=(-0.362, 0.083), resolution=(1280, 720)),intervalfunc=main)

                touch(Template(r"tpl1605989397146.png", record_pos=(-0.362, 0.083), resolution=(1280, 720)))
            elif exists(Template(r"tpl1605989514414.png", record_pos=(0.362, 0.23), resolution=(1280, 720))):
                wait(Template(r"tpl1605989514414.png", record_pos=(0.362, 0.23), resolution=(1280, 720)),intervalfunc=main)
                touch(Template(r"tpl1605989514414.png", record_pos=(0.362, 0.23), resolution=(1280, 720)))
            elif exists(Template(r"tpl1605944094403.png", record_pos=(-0.466, -0.247), resolution=(1280, 720))):
                wait(Template(r"tpl1605944094403.png", record_pos=(-0.466, -0.247), resolution=(1280, 720)),intervalfunc=main)
                touch(Template(r"tpl1605944094403.png", record_pos=(-0.466, -0.247), resolution=(1280, 720)))
            elif exists(Template(r"tpl1605992707698.png", record_pos=(0.0, -0.003), resolution=(1280, 720))):
                sys.exit(0)
            else:
                main()
             
main()

auto_setup(__file__)


