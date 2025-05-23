import re
from qt_graph import Analysis_qt_graph

from PySide6.QtWidgets import QApplication 
from PySide6.QtUiTools import QUiLoader
import pyqtgraph as pg
from datetime import datetime

log_file_path = './robot_bms_soc.log'

class Analysis_log:
        def __init__(self):
                self.log_file_path = log_file_path
                # set regular expression
                self.timestamp_pattern = r'\[(.*?)\]'
                self.voltage_pattern = r'voltage:\s*([-\d.]+)'
                self.percentage_pattern = r'percentage:\s*([-\d.]+)'
                self.data_voltage = []
                self.data_percentage = []
                
        def loop_extraction(self):
                print(f'enter loop_extraction...')
                with open(self.log_file_path, 'r') as file:
                        log_content = file.readlines()
                
                for line in log_content:
                        timestamp_match = re.search(self.timestamp_pattern, line)
                        voltage_match = re.search(self.voltage_pattern, line)
                        percentage_match = re.search(self.percentage_pattern, line)
                                                                      
                        if timestamp_match:
                                timestamp = timestamp_match.group(1)
                                timestamp_dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                                float_timestamp = timestamp_dt.timestamp()
                                if voltage_match:
                                        voltage = float(voltage_match.group(1))
                                        self.data_voltage.append((float_timestamp, voltage))
                                if percentage_match:
                                        percentage = float(percentage_match.group(1))
                                        self.data_percentage.append((float_timestamp, percentage))
                
                self.data_voltage.sort(key=lambda x: x[0])
                self.data_percentage.sort(key=lambda x: x[0])
        
                # for entry in self.data_voltage:
                #         print(f'Timestamp: {entry[0]}, Voltage: {entry[1]}')
                # for entry in self.data_percentage:
                #         print(f'Timestamp: {entry[0]}, Percentage: {entry[1]}')
                        
        def return_data_voltage(self):
                return self.data_voltage
        
        def return_data_percentage(self):
                return self.data_percentage
        
if __name__ == "__main__":
        app = QApplication()
        log_analyzer = Analysis_log()
        log_analyzer.loop_extraction()
        qt_graph_analyzer = Analysis_qt_graph(log_analyzer.return_data_voltage(), log_analyzer.return_data_percentage())
        qt_graph_analyzer.show()
        app.exec()
        