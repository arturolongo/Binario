import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self, cinta):
        self.cinta = list(cinta)
        self.posicion = 0
        self.estado_actual = 'q0'
        self.resultado = 2

    def avanzar(self):
        transiciones = {
            'q0': {'1': ('q1', '1', 'R')},
            'q1': {'0': ('q2', '0', 'R')},
            'q2': {'=': ('q3', '=', 'R'), '0': ('q2', '0', 'R'), '1': ('q2', '1', 'R')},
            'q3': {'0': ('q3', '0', 'R'), '1': ('q3', '1', 'R'), 'B': ('qF', 'B', 'R')}
        }

        simbolo_actual = self.cinta[self.posicion]

        if self.estado_actual in transiciones and simbolo_actual in transiciones[self.estado_actual]:
            nuevo_estado, simbolo_escrito, direccion = transiciones[self.estado_actual][simbolo_actual]
            self.cinta[self.posicion] = simbolo_escrito
            self.estado_actual = nuevo_estado

            self.posicion += 1 if direccion == 'R' else -1

            if self.estado_actual == 'q3' and simbolo_actual == '1':
                self.resultado += 1

    def ejecutar(self):
        while self.estado_actual != 'qF':
            if self.posicion < 0 or self.posicion >= len(self.cinta):
                break
            self.avanzar()
        return self.resultado

class MinimalTuringInterface:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Turing - Suma Binaria")
        self.raiz.geometry("320x200")
        self.raiz.configure(bg="#1C1C1C")  # Fondo oscuro

        self.entrada = tk.Entry(self.raiz, justify='center', font=("Arial", 14), bg="#2E2E2E", fg="white", bd=0)
        self.entrada.pack(pady=20, ipady=5, fill='x', padx=30)

        self.boton = tk.Button(self.raiz, text="Ejecutar", command=self.sumar_binarios, 
                               bg="#4A4A4A", fg="white", font=("Arial", 12), bd=0)
        self.boton.pack(pady=10)

        self.resultado_binario = tk.Label(self.raiz, text="", bg="#1C1C1C", fg="white", font=("Arial", 12))
        self.resultado_binario.pack(pady=5)

    def sumar_binarios(self):
        binario = self.entrada.get().strip()
        if not all(d in '01' for d in binario):
            messagebox.showerror("Error", "Solo se permiten números binarios (0 y 1).")
            return

        cinta = f"10={binario}B"
        maquina = TuringMachine(cinta)
        resultado = maquina.ejecutar()

        resultado_bin = bin(resultado)[2:]
        self.resultado_binario.config(text=f"Resultado: {resultado_bin} (binario)")

if __name__ == "__main__":
    raiz = tk.Tk()
    app = MinimalTuringInterface(raiz)
    raiz.mainloop()
