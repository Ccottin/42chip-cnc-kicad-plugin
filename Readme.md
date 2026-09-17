# Kicad plugin for CNC minimal requirements in 42Chips' lab 

The goal is simple : get the plugin, press the button inside PCB designer & all correct constraints will be setted for an optimal use of the CNC machine we use to drill PCB at school :)

### Difficulties and solutions 

The main problem encoutered is the current migration inside kicad's plugin library. Kicad dev are moving from a the SWIG-based API (connects programs with scripts so functions can be called accross languages) to an IPC (processes communicate directly & share data across system).
The SWIG will stop working at version 11.0, but it holds all the functions we'll need. Thoses functions won't be available onthe IPC's lib before 11.0 

__SWIG = Simplified Wrapper ans Inteface Generator__
__IPC = Inter-Process Communication__

So, this pluggin should handle both APIs according to your Kicad's version :D

# 


[Plugin inspiration to handle 9.0, 10.0 and 11.0 at same time](https://github.com/hulryung/kicad-lcsc-manager/blob/main/metadata.json)

[Publishing an add-on](https://dev-docs.kicad.org/en/addons/)