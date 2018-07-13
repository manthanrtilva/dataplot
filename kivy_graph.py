
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot
from kivy.garden.graph import LinePlot
from kivy.clock import Clock
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.colorpicker import ColorPicker

import h5py
import numpy as np 
import time
import random

from functools import partial


class Logic(BoxLayout):
    def __init__(self,):
        super(Logic, self).__init__()
        self.setMinMax = False
        self.plotdata = {}
        self.color = [1,1,1,1]
        for datapoint in f:
            Clock.schedule_once(partial(self.addGraph,datapoint,f[datapoint][0],f[datapoint][1]), 2)

    def addGraph(self,datapoint,xData,yData,dt):
        points = [t for t in zip((xData).astype(int),yData)];
        ymin = int(min(yData))
        ymax = int(max(yData))
        xmin = int(min(xData))
        xmax = int(max(xData))

        if self.setMinMax :
            if self.ids.graph.ymin > ymin:
                self.ids.graph.ymin = ymin
            if self.ids.graph.ymax < ymax:
                self.ids.graph.ymax = ymax
            if self.ids.graph.xmin > xmin:
                self.ids.graph.xmin = xmin
            if self.ids.graph.xmax < xmax:
                self.ids.graph.xmax = xmax  
        else:
            self.ids.graph.ymin = ymin
            self.ids.graph.ymax = ymax
            self.ids.graph.xmin = xmin
            self.ids.graph.xmax = xmax  
            self.setMinMax = True

        plot = LinePlot(color=self.color)
        plot.points = points
        self.ids.graph.add_plot(plot)
        index = random.randint(0,3)
        btn1 = ToggleButton(text=datapoint,background_color=self.color)
        btn1.bind(state=partial(self.on_press,datapoint))
        cp = ColorPicker(color=self.color)
        cp.bind(color=partial(self.on_color,datapoint))
        self.plotdata[datapoint] = {'color':self.color,'button':btn1,'plot':plot,'colorpick':cp,'points':points}
        self.color[index]=self.color[index] - (random.random());
        self.ids.hBox.add_widget(btn1)
        self.ids.hBoxColor.add_widget(cp)

    def start(self,min,max,dt):
        self.ids.graph.ymin = int(min)
        self.ids.graph.ymax = int(max)
        self.ids.graph.add_plot(self.plot)

    def on_color(self,datapoint,instance, value):
        self.plotdata[datapoint]['color'] = value
        # print(datapoint+":RGBA = "+ str(value))
        self.plotdata[datapoint]['plot'].color = value
        # self.plotdata[datapoint]['plot'].draw()
        self.ids.graph.remove_plot(self.plotdata[datapoint]['plot'])
        points = self.plotdata[datapoint]['points']
        self.plotdata[datapoint]['plot'] = LinePlot(color=value)
        self.plotdata[datapoint]['plot'].points = points
        self.plotdata[datapoint]['points'] = points
        self.plotdata[datapoint]['button'].background_color = value
        self.ids.graph.add_plot(self.plotdata[datapoint]['plot'])
        

    def on_press(self,datapoint,instance,state):
        if state == "normal":
            self.showPlot(datapoint)
        else:
            self.hidePlot(datapoint)

    def hidePlot(self,datapoint):
        self.ids.graph.remove_plot(self.plotdata[datapoint]['plot'])

    def showPlot(self,datapoint):
        self.ids.graph.add_plot(self.plotdata[datapoint]['plot'])




class PlotDatas(App):
    def build(self):
        return Builder.load_file("look.kv")

if __name__ == "__main__":
    levels = []  # store levels of microphone
    f = h5py.File('sample.hdf5', 'r')
    PlotDatas().run()
    