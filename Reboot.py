import array, os, sys
import time
from MySQLdb import *
import sqlite3 as sql
class Reboot:
    def __init__(self):
        self.acionado = False
        self.nome = "Otto"
        self.input = input("Digite: ")
        self.contador = 0
        self.opções = ["Salvar", "Deletar", "Fechar"]
        self.elementos = ["Fogo", "Agua", "Terra", "Ar"]
        self.dicts = {0 : "Calor", 1 : "mutação", 2: "Pacividade", 3 : "Força e imponencia"}
    def analisador(self, elem : array):
        for i in elem:
            if i == elem[0]:
                print("Tudo ativado")
        try:
            for i in range(len(self.opções)):
                if self.input == self.opções[0]:
                    self.save()
        except Exception as exc:
            print(exc)
    def save(self):
        with open("damocles", "w") as file:
            file.write(str(self.input))
    def temporizador(self):
        if self.contador == 0:
            for i in range(len(self.elementos)):
                self.contador += 1
                time.sleep(2)
                if self.contador >= 20:
                    self.acionado = False
                    break
                if self.contador >= i and self.contador <= 30:
                    return True
                elif self.contador == 20:
                    return False
    def main(self):
        count = 0
        if self.temporizador():
            self.acionado = True
        while self.acionado:
            count += 1
            self.analisador(self.elementos)
            if count == 10:
                self.acionado = False
                break

if __name__ == "__main__":
    reboot = Reboot()
    reboot.main()
