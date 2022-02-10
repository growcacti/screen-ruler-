from tkinter import *
from random import *

window = Tk()
window.title('screen ruler')

##def rulerline():
##    width = 1600
##    height = 100
##    canvas = Canvas(window, background='white', width=width, height=height)
##


    
def create_grid():
    width = 40
    height = 1000
    canvas = Canvas(window, background='blue', width=width, height=height)

    

    for line in range(0, width, 10): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w', width=1)

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h', width=1)

    for line in range(1000, 40, 100): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='light blue', tags='grid_line_w', width=3)

    for list in range(100, 1000, 100): # range(start, stop, step)
        canvas.create_text(20, list , text=list, fill="orange",font=('Helvetica 12 bold'))    

    
    ##canvas.create_text(100, 100, text= "Some Text",fill="black",font=('Helvetica 15 bold'))
##    for line in range(60, 80, 20):
##        canvas.create_line([(0, line), (width, line)], fill='light blue', tags='grid_line_h',width=5)
##
##    for line in range(700, 740 , 20): # range(start, stop, step)
##        canvas.create_line([(line, 0), (line, height)], fill='orange', tags='grid_line_w', width=5)
##
##    for line in range(20, 1000, 20):
##        canvas.create_line([(0, line), (width, line)], fill='orange', tags='grid_line_h', width=5)
##
##    
##






        
##    for line in range(60, 80, 20):
##        canvas.create_line([(0, line), (width, line)], fill='light blue', tags='grid_line_h',width=5)
##
##    for line in range(700, 740 , 20): # range(start, stop, step)
##        canvas.create_line([(line, 0), (line, height)], fill='orange', tags='grid_line_w', width=5)
##
##    for line in range(20, 1000, 20):
##        canvas.create_line([(0, line), (width, line)], fill='orange', tags='grid_line_h', width=5)
##
##    
##
    canvas.grid(row=0, column=0)
create_grid()


    
##    line11 = canvas.create_line(20, 70, 1800, 70 , fill ='black', width = 7)
##
##    line12 = canvas.create_line(600, 20, 600, 1000, fill ='black', width = 7)
##
##    line13 = canvas.create_line(20, 60, 20, 80, fill ='black', width = 7)
##
##    line14 = canvas.create_line(40 ,60, 40, 80, fill ='black', width = 7)
##
##    line15 = canvas.create_line(60, 60, 220, 80, fill ='black', width = 7)
##
##    line16 = canvas.create_line(80, 60,  80, 80, fill ='black', width = 7)
##
##    line17 = canvas.create_line(100, 60, 100, 80, fill ='black', width = 7)
##
##    line18 = canvas.create_line(120, 60, 120, 80, fill ='black', width = 7)
##
##    line19 = canvas.create_line(140,  60, 140, 80, fill ='black', width = 7)
##
##    line20 = canvas.create_line(160, 60, 160, 80, fill ='black', width = 7)
##

##    line21 = canvas.create_line(60, 70, 60, 90 , fill ='black', width = 7)
##
##    line22 = canvas.create_line(60, 90, 60, 120, fill ='black', width = 7)
##
##    line23 = canvas.create_line(60,120, 220, 140 , fill ='black', width = 7)
##
##    line24 = canvas.create_line(220,140, 60,160 , fill ='black', width = 7)
##
##    line25 = canvas.create_line(60,160, 220,60, fill ='black', width = 7)
##
##    line26 = canvas.create_line(220,60, 60,200, fill ='black', width = 7)
##
##    line27 = canvas.create_line(60,200, 220,220, fill ='black', width = 7)
##
##    line28 = canvas.create_line(220,220, 60,240 , fill ='black', width = 7)
##
##    line29 = canvas.create_line(60,240, 60,350 , fill ='black', width = 7)
##
##    lin310 = canvas.create_line(60, 70, 60, 90 , fill ='black', width = 7)
##    
##
##    line22 = canvas.create_line(60, 90, 60, 120, fill ='black', width = 7)
##
##    line23 = canvas.create_line(60,120, 220, 140 , fill ='black', width = 7)
##
##    line24 = canvas.create_line(220,140, 60,160 , fill ='black', width = 7)
##
##    line25 = canvas.create_line(60,160, 220,60, fill ='black', width = 7)
##
##    line26 = canvas.create_line(220,60, 60,200, fill ='black', width = 7)
##
##    line27 = canvas.create_line(60,200, 220,220, fill ='black', width = 7)
##
##    line28 = canvas.create_line(220,220, 60,240 , fill ='black', width = 7)
##
##    line29 = canvas.create_line(60,240, 60,350 , fill ='black', width = 7)
##
##    lin200 = canvas.create_line(60, 70, 60, 90 , fill ='black', width = 7)
##
##    lin201 = canvas.create_line(60, 90, 60, 120, fill ='black', width = 7)
##
##    lin202 = canvas.create_line(60,120, 220, 140 , fill ='black', width = 7)
##
##    lin203 = canvas.create_line(220,140, 60,160 , fill ='black', width = 7)
##
##    line35 = canvas.create_line(60,160, 220,60, fill ='black', width = 7)
##
##    line36 = canvas.create_line(220,60, 60,200, fill ='black', width = 7)
##
##    line37 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line38 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line39 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##
##
##    line41 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line42 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line43 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line44 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line45 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line46 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line47 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line48 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line49 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    line51 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line52 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line53 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line54 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line55 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line56 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line57 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line58 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line59 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    line61 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line62 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line63 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line64 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line65 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line66 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line67 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line68 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line69 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    line71 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line72 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line73 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line74 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line75 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line76 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line77 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line78 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line79 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    line81 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line82 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line83 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line84 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line85 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line86 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line87 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line88 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line89 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    line90 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line91 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line92 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line93 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line95 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line96 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line97 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line98 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line99 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    line101 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line102 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line103 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line104 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line105 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line106 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line107 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line108 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line109 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    line110 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line111 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line112 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line113 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line114 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line115 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line116 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line117 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line118 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    line119 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line120 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##    line121 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line122 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##
##    line123 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line124 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line125 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line126 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line127 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line128 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line129 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##    line130 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line131 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line132 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line133 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line134 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line135 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line136 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line137 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line138 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line139 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line140 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line141 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line142 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line143 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line144 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line145 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line146 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line147 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line148 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line149 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line150 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line151 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##
##
##
##
##    line152 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line153 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line154 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line155 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line156 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line157 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line158  = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line159 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line160 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    line161 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line162 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line163 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line164 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line165 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line166 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line167 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line168 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line169 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    line170 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line171 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line172 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line173 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line174 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line175 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line176 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line177 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line178 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##
##    line179 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line180 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line181 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line182 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line183 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line184 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line185 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line186 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line187 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    line190 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line191 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line192 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line193 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line194 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line195 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line196 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line197 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line198 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    lin11 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    lin12 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    lin13 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    lin14 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    lin15 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    lin16 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    lin17 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    lin18 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    lin19 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    lin20 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##
##    lin21 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    lin22 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    lin23 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    lin24 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    lin25 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    lin26 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    lin27 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    lin28 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    lin29 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    lin30 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    lin31 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    lin32 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    lin33 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    lin34 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    lin36 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    lin37 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    lin38 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    lin39 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    lin200 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    lin201 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    lin202 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    lin203 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    lin40 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    lin41 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    lin42 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    lin43 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line44 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##
##
##    lin441 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    lin442 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    lin443 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    lin444 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    lin445 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    lin446 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    lin447 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    lin448 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    lin449 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    lin451 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    lin452 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    lin453 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    lin454 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    lin455 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    lin456 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    lin457 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    lin458 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    lin459 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    lin461 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    lin462 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    lin563 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    lin564 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    lin565 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    lin566 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    lin567 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    lin568 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    lin569 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    lin571 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    lin572 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    lin573 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    lin574 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    lin575 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    lin576 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    lin577 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    lin578 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    lin579 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    lin581 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##    lin582 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    lin683 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line684 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line865 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line866 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line876= canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    li45 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    li4589 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    li90 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    li91 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li92 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    li3 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    li95 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    li96 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    li97 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    li98 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    li99 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    li101 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    lie102 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##    lie103 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    lie104 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    lie105 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    lie106 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    lie107 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    lie108 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    lie109 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    lie110 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    lie111 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    lie112 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    lie113 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    lie114 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    lie115 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    lie116 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    lie117 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    lie118 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##
##    lie119 = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    lie120 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##    li1121 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##    li7122 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##
##    l3 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    l4 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    l5 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    l6 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    l7 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    l8 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    l9 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
##    li0 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li31 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li132 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li33 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li134 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li135 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li136 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li137 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li138 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li139 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li140 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li141 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li142 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li143 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li144 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li145 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li146 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li147 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    li148 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##

window.mainloop()
