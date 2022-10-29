#!/usr/bin/python3

import PySimpleGUI as sg
import table_info_window
import database_interface
import os
import os.path
from os import path


if path.exists('iptables_database.db') == True:
  pass
else:
  import create_database
  exec("create_database")

if  path.exists('iptables.rules') == True:
  pass
else:
  cmd = "sudo iptables-save > iptables.rules"
  os.system(cmd)


layout = [
    [sg.Text("Chain:", size=(20, 1))],
    [sg.Combo(["Input","Forward","Output"],default_value="Input",key="-CHAIN-")],
    [sg.Text("Enter Target:", size=(20, 1))],
    [sg.Combo(["Accept","Drop","Reject"],default_value="Accept",key="-TARGET-")],
    [sg.Text("Enter Proto:"), sg.Input(key='-PROTO-', do_not_clear=False, size=(20, 1))],
    [sg.Text("Enter Opt:"), sg.Input(key='-OPT-', do_not_clear=False, size=(20, 1))],
    [sg.Text("Port:"), sg.Input(key='-PORT-', do_not_clear=False, size=(20, 1))],
    [sg.Text("Enter Source IP:"), sg.Input(key='-SRC_IP-', do_not_clear=False, size=(20, 1))],
    [sg.Text("Dest IP:"), sg.Input(key='-DEST_IP-', do_not_clear=False, size=(20, 1))],
    
    [sg.Button('Submit Info'), sg.Button('Show Table'), sg.Exit()]
]


window = sg.Window("Submit Info", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
      break
    elif event == 'Submit Info':
      database_interface.insert_rules(values['-CHAIN-'], values['-TARGET-'], values['-PROTO-'], values['-OPT-'], values['-PORT-'], values['-SRC_IP-'], values['-DEST_IP-'])
      L = "-A" + " " + str(values['-CHAIN-']) + " " + str(values['-PROTO-']) + " " + str(values['-OPT-']) + " " + str(values['-SRC_IP-']) + " " + str(values['-DEST_IP-']) + " " + str(values['-PORT-']) + " " + str(values['-TARGET-']) + "\n"
      inputfile = open('iptables.rules', 'r').readlines()
      write_file = open('iptables.rules','w')
      for line in inputfile:
        write_file.write(line)
        if ':OUTPUT ACCEPT' in line:
          for item in L:
            new_line = item        
            write_file.write(new_line) 
      write_file.close()
      cmd2 = "sudo iptables-restore < iptables.rules"
      os.system(cmd2)

      sg.popup('Rules Submitted')
    elif event == 'Show Table':
      table_info_window.create()

window.close()
      