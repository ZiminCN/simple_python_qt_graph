from PySide6.QtWidgets import QApplication 
from PySide6.QtUiTools import QUiLoader
import pyqtgraph as pg
# paramenter[] = [(timestamp, data)...]

class Analysis_qt_graph:
        def __init__(self, paramenter_1, paramenter_2):
                self.file_name = 'res/test_py_graph.ui'
                self.loade = QUiLoader()
                self.loade.registerCustomWidget(pg.PlotWidget) # 注册PlotWidget类
                self.file_ui_1 = self.loade.load(self.file_name) # 加载ui文件
                self.file_ui_2 = self.loade.load(self.file_name) # 加载ui文件
                self.raw_paramenter_1 = paramenter_1
                self.raw_paramenter_2 = paramenter_2
                self.timestamp_1 = []
                self.timestamp_2 = []
                self.float_timestamp_1 = []
                self.float_timestamp_2 = []
                self.data_1 = []
                self.data_2 = []
                self.timestamp_1, self.data_1 = self.decode_paramenter(self.raw_paramenter_1)
                self.timestamp_2, self.data_2 = self.decode_paramenter(self.raw_paramenter_2)
                
                self.file_ui_1.graphicsView.setBackground('w') # 设置背景颜色为白色
                self.file_ui_2.graphicsView.setBackground('w') # 设置背景颜色为白色
                pen = pg.mkPen(color = (255 , 0 , 0) , width = 15) # 设置曲线颜色为红色,宽度设置为15个像素点
                pen1 = pg.mkPen(color = (0 , 0 , 255) , width = 15) # 设置曲线颜色为蓝色,宽度设置为15个像素点
                styles ={'color':'r' , 'font-size':'30px'} # 设置标签的颜色和大小
                
                
                self.file_ui_1.graphicsView.setLabel('bottom'  , '时间' , **styles) # 设置底部X的标签名字为温度
                self.file_ui_1.graphicsView.setLabel('left'  , '电压' , **styles) # 设置左边Y的标签名字为电压
                self.file_ui_1.graphicsView.showGrid(x = True , y = True) # X轴和Y轴的网格显示
                self.file_ui_1.graphicsView.setTitle('电池电压/时间图' , color = 'r' , size = '15pt') # 设置标题为绘图界面
                self.file_ui_1.graphicsView.plot(self.timestamp_1 , self.data_1 ,pen = pen) # 第一条曲线
                
                self.file_ui_2.graphicsView.setLabel('bottom'  , '时间' , **styles) # 设置底部X的标签名字为温度
                self.file_ui_2.graphicsView.setLabel('left'  , 'SOC' , **styles) # 设置左边Y的标签名字为电压
                self.file_ui_2.graphicsView.showGrid(x = True , y = True) # X轴和Y轴的网格显示
                self.file_ui_2.graphicsView.setTitle('电池SOC/时间图' , color = 'r' , size = '15pt') # 设置标题为绘图界面
                self.file_ui_2.graphicsView.plot(self.timestamp_2 , self.data_2 ,pen = pen1) # 第一条曲线

                
        def decode_paramenter(self, paramenter):
                temp_timestamp = []
                temp_data = []
                for entry in paramenter:
                        temp_timestamp.append(entry[0])
                        temp_data.append(entry[1])
                
                return temp_timestamp, temp_data

        # 显示界面
        def show(self): 
                self.file_ui_1.show()
                self.file_ui_2.show()
        
        
                