from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

FILE_UI = 'main_window.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(FILE_UI, self)
        
        self.calc_button.clicked.connect(self.calcular)
        
    def calcular(self):
        nome = self.nome.text()
        hrs_d = int(self.hora_dia.text())
        dia_s = int(self.dia_semana.text())
        anual = float(self.anual.text())
        mes = anual/12
        semana = mes/4.34
        dia = semana/dia_s
        hora = dia/hrs_d
        
        """Tabela de informações inseridas"""
        self.label_name.setText(str(f' {nome}'))
        self.label_hour.setText(str(f' Horas de trabalho por dia: {hrs_d}'))
        self.label_days.setText(str(f' Dias de trabalho por semana: {dia_s}'))
        self.label_anual.setText(str(f' R$ {anual}'))
        
        """Tabela de dados calculados"""
        self.s_hora.setText(str(f'Salário por Hora: {hora:.2f}'))
        self.s_dia.setText(str(f'Salário Diário: {dia:.2f}'))
        self.s_semana.setText(str(f'Salário Semanal: {semana:.2f}'))
        self.s_mes.setText(str(f'Salário Mensal: {mes:.2f}'))
        self.s_anual.setText(str(f'Salário Anual: {anual}'))