from graphics import *
#Constants
#Window Size
WIN_HEIGHT = 900
WIN_WIDTH = 1600
WIN_BACK_COLOR = "black"

NO_OF_BANDS=10
BORDER_PADDING=100
BAR_WIDTH=50
BAR_HEIGHT=500
BAR_Y_TOP=WIN_HEIGHT-BORDER_PADDING-BAR_HEIGHT

AVAIL_WIDTH = WIN_WIDTH-BORDER_PADDING*2;
INTER_BAND_GAP=(AVAIL_WIDTH-NO_OF_BANDS*BAR_WIDTH)/(NO_OF_BANDS-1)+BAR_WIDTH

WIN = GraphWin("Graphic Visualizer", WIN_WIDTH, WIN_HEIGHT)

def draw_Rectangle(x, y, width, height,out_color, fill_color):
        r = Rectangle(Point(x, y), Point(x+width,y+height))
        r.setOutline(out_color)
        r.setFill(fill_color)
        r.draw(WIN)

def draw_Text(x, y, text, color):
        t=Text(Point(x, y), text)
        t.setOutline(color)
        t.draw(WIN)

def graphics_setup(freqlist):
        WIN.setBackground(WIN_BACK_COLOR)
        for i in range(NO_OF_BANDS):
                x_top_left = BORDER_PADDING + i*INTER_BAND_GAP
                draw_Rectangle(x_top_left, BAR_Y_TOP, BAR_WIDTH, BAR_HEIGHT, "white", "black")
                draw_Text(x_top_left + BAR_WIDTH/2, BAR_Y_TOP + BAR_HEIGHT + 10, str(freqlist[i]) + "Hz", "white")

def graphics_update_levels(freq_levels):
        for i in range(NO_OF_BANDS):
                current_freq_height = BAR_HEIGHT * freq_levels[i]
                x_top_left = BORDER_PADDING + i*INTER_BAND_GAP
                y_top_left = BAR_Y_TOP + BAR_HEIGHT - current_freq_height
                #erase previous level
                draw_Rectangle(x_top_left, BAR_Y_TOP, BAR_WIDTH, BAR_HEIGHT, "white", "black")
                #draw new level
                draw_Rectangle(x_top_left, y_top_left, BAR_WIDTH, current_freq_height, "white", "green")

def graphics_shutdown():
        WIN.close()
        
