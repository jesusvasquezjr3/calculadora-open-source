import tkinter as tk
from tkinter import ttk, messagebox
import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Open Source")
        self.root.geometry("600x700")
        self.root.configure(bg='black')
        self.root.resizable(False, False)
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()
        
        # Variables para las entradas
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.nums_avanzados_var = tk.StringVar()
        
        self.create_widgets()
        
    def configure_styles(self):
        # Configurar estilos para widgets
        self.style.configure('Black.TFrame', background='black')
        self.style.configure('Black.TLabel', background='black', foreground='white', font=('Arial', 12))
        self.style.configure('Title.TLabel', background='black', foreground='white', font=('Arial', 16, 'bold'))
        self.style.configure('Black.TEntry', fieldbackground='black', foreground='white', borderwidth=2, relief='solid')
        self.style.configure('Black.TButton', background='black', foreground='white', borderwidth=2, relief='solid', font=('Arial', 10))
        self.style.map('Black.TButton', background=[('active', '#333333')])
        
    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, style='Black.TFrame', padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(main_frame, text="CALCULADORA", style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Separador
        separator = tk.Frame(main_frame, height=2, bg='white')
        separator.pack(fill=tk.X, pady=(0, 20))
        
        # Frame para operaciones básicas
        basic_frame = ttk.Frame(main_frame, style='Black.TFrame')
        basic_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(basic_frame, text="OPERACIONES BÁSICAS", style='Black.TLabel').pack(pady=(0, 10))
        
        # Entrada número 1
        ttk.Label(basic_frame, text="Número 1:", style='Black.TLabel').pack(anchor=tk.W)
        entry1 = ttk.Entry(basic_frame, textvariable=self.num1_var, style='Black.TEntry', width=30)
        entry1.pack(pady=(0, 10), ipady=5)
        
        # Entrada número 2
        ttk.Label(basic_frame, text="Número 2:", style='Black.TLabel').pack(anchor=tk.W)
        entry2 = ttk.Entry(basic_frame, textvariable=self.num2_var, style='Black.TEntry', width=30)
        entry2.pack(pady=(0, 10), ipady=5)
        
        # Botones de operaciones
        buttons_frame = ttk.Frame(basic_frame, style='Black.TFrame')
        buttons_frame.pack(pady=(0, 10))
        
        ttk.Button(buttons_frame, text="SUMAR", command=self.sumar, style='Black.TButton').grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(buttons_frame, text="RESTAR", command=self.restar, style='Black.TButton').grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(buttons_frame, text="MULTIPLICAR", command=self.multiplicar, style='Black.TButton').grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(buttons_frame, text="DIVIDIR", command=self.dividir, style='Black.TButton').grid(row=1, column=1, padx=5, pady=5)
        
        # Separador
        separator2 = tk.Frame(main_frame, height=2, bg='white')
        separator2.pack(fill=tk.X, pady=(0, 20))
        
        # Frame para suma avanzada
        advanced_frame = ttk.Frame(main_frame, style='Black.TFrame')
        advanced_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(advanced_frame, text="SUMA AVANZADA", style='Black.TLabel').pack(pady=(0, 10))
        
        # Entrada números múltiples
        ttk.Label(advanced_frame, text="Números (separados por comas):", style='Black.TLabel').pack(anchor=tk.W)
        entry_advanced = ttk.Entry(advanced_frame, textvariable=self.nums_avanzados_var, style='Black.TEntry', width=30)
        entry_advanced.pack(pady=(0, 10), ipady=5)
        
        ttk.Button(advanced_frame, text="SUMAR MÚLTIPLES", command=self.suma_avanzada, style='Black.TButton').pack(pady=(0, 10))
        
        # Separador
        separator3 = tk.Frame(main_frame, height=2, bg='white')
        separator3.pack(fill=tk.X, pady=(0, 20))
        
        # Frame para resultado
        result_frame = ttk.Frame(main_frame, style='Black.TFrame')
        result_frame.pack(fill=tk.X)
        
        ttk.Label(result_frame, text="RESULTADO:", style='Black.TLabel').pack(anchor=tk.W)
        result_entry = ttk.Entry(result_frame, textvariable=self.result_var, style='Black.TEntry', width=30, state='readonly')
        result_entry.pack(pady=(0, 10), ipady=5)
        
        # Botón limpiar
        ttk.Button(result_frame, text="LIMPIAR", command=self.limpiar, style='Black.TButton').pack()
        
    def sumar(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            resultado = sumar.sumar(num1, num2)
            self.result_var.set(str(resultado))
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la operación: {str(e)}")
    
    def restar(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            resultado = resta.restar(num1, num2)
            self.result_var.set(str(resultado))
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la operación: {str(e)}")
    
    def multiplicar(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            resultado = multiplicacion.multiplicar(num1, num2)
            self.result_var.set(str(resultado))
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la operación: {str(e)}")
    
    def dividir(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            resultado = dividir.dividir(num1, num2)
            self.result_var.set(str(resultado))
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la operación: {str(e)}")
    
    def suma_avanzada(self):
        try:
            nums_str = self.nums_avanzados_var.get()
            if not nums_str:
                messagebox.showerror("Error", "Por favor ingrese números separados por comas")
                return
            
            nums = [float(x.strip()) for x in nums_str.split(',')]
            resultado = suma_avanzada.suma_avanzada(nums)
            self.result_var.set(str(resultado))
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos separados por comas")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la operación: {str(e)}")
    
    def limpiar(self):
        self.num1_var.set("")
        self.num2_var.set("")
        self.result_var.set("")
        self.nums_avanzados_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()