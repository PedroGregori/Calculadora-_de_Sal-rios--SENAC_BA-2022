from PyQt5.QtWidgets import QApplication
import sys
from main_window import MainWindow

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()


"""nome = input("Escreva seu nome completo: ")
hrs_d = int(input("Quantas horas você trabalha por dia?: "))
dias_s = int(input("Quantos dias você trabalha por semana?: "))
anual = float(input("Qual o seu salário anual?: "))
mes = anual/12
semana = mes/4.34
dia = semana/dias_s
hora = dia/hrs_d

print(f'Salário por hora: R$" {hora:.2f}')
print(f'Salário por dia: R$" {dia:.2f}')
print(f'Salário por semana: R$" {semana:.2f}')
print(f'Salário por mês: R$" {mes:.2f}')
print("Salário anual: R$",anual)"""
