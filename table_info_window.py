#!/usr/bin/python3

import PySimpleGUI as sg
import database_interface

def edit_cell(table_info_window, key, row, col, justify='left'):
  
  global textvariable, edit

  def callback(event, row, col, text, key):
    global edit
    widget= event.widget 
    if key == "Return":
      text = widget.get()
    widget.destroy()
    widget.master.destroy()

    values = list(table.item(row, 'values'))
    values[col] = text
    table.item(row, values=values)
    edit = False
    
    

  if edit or row <= 0:
      return

  edit = True 

  root = table_info_window.TKroot
  table = table_info_window[key].Widget
  
  text = table.item(row, "values")[col]
  x, y, width, height = table.bbox(row, col)

  frame = sg.tk.Frame(root)
  frame.place(x=x, y=y, anchor="nw", width=width, height=height)

  textvariable = sg.tk.StringVar()
  textvariable.set(text)

  entry = sg.tk.Entry(frame, textvariable=textvariable, justify=justify)
  entry.pack()
  entry.select_range(0, sg.tk.END)
  entry.icursor(sg.tk.END)
  entry.focus_force()


  entry.bind("<Return>", lambda e, r=row, c=col, t=text, k="Return":callback(e, r, c, t, k))
  

  
  



def create():

  

  global edit

  edit = False

  sg.set_options(dpi_awareness=True)

  contact_rules = database_interface.retrieve_rules()
  headings = ['Chain', 'Allow/Block', 'Proto', 'Opt', 'Port','Source IP', 'Dest IP']
  table_info_window_layout = [
    [sg.Table(values=contact_rules,
      headings=headings, 
      max_col_width=35,
      auto_size_columns=True,
      display_row_numbers=True,
      justification='right',
      num_rows=10,
      enable_events=True,
      key='-TABLE-',
      row_height = 35,
      enable_click_events=True,
      tooltip='Reservation Table')],
    
    [sg.Text('Cell clicked:'), sg.T(key='-CLICKED_CELL-')]

   ]
  
  
  table_info_window = sg.Window('Table Information Window',             table_info_window_layout, modal=True, finalize=True)
  
  while True:
    event, value = table_info_window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
      break
    elif isinstance(event, tuple):
      if isinstance(event[2][0], int) and event[2][0] > -1:  
        cell = row, col= event[2]
        table_info_window['-CLICKED_CELL-'].update(cell)
        edit_cell(table_info_window, '-TABLE-', row+1, col, justify='right')
      
    #if event == '-TABLE-':
      #print(values['-TABLE-'][0])
      #selected_row_index = values['-TABLE-'][0]
      #table_info = table_info_array[selected_row_index]
 #creates popup when you click on a row      
      #popup_message = "Rule: " + table_info[0] + '\n' + "Proto: " + table_info[1] + '\n' + "SRC IP: " + table_info[3]
      #sg.popup(popup_message)
      
      
      

  table_info_window.close()
    