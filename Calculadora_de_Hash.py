import hashlib
import tkinter as tk
from tkinter import filedialog
import os

class ChooseSourceTypeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Seleção de Fonte de Dados")

        self.selection_var = tk.StringVar()
        self.selection_var.set("file")

        self.label = tk.Label(root, text="Escolha a Origem dos Dados:", font=("Arial", 14))
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky='w')

        self.file_radio = tk.Radiobutton(root, text="Arquivo", variable=self.selection_var, value="file", font=("Arial", 12))
        self.file_radio.grid(row=1, column=0, padx=20, pady=5, sticky='w')

        self.text_radio = tk.Radiobutton(root, text="Texto", variable=self.selection_var, value="text", font=("Arial", 12))
        self.text_radio.grid(row=2, column=0, padx=20, pady=5, sticky='w')

        self.continue_button = tk.Button(root, text="Continuar", command=self.continue_to_calculator, font=("Arial", 12))
        self.continue_button.grid(row=3, column=0, padx=20, pady=20, sticky='w')

        centralize_screen(root)

    def continue_to_calculator(self):
        clear_screen(root)
        HashCalculator(root, self.selection_var.get())

class HashCalculator:
    def __init__(self, root, is_file):
        self.root = root
        self.root.title("Calculadora de Hash")

        self.entryTextLabel = tk.Label(root, text="Texto: ", font=("Arial", 14))
        self.entryTextLabel.grid(row=0, column=0, padx=20, pady=20, sticky='w')

        self.entryText = tk.Entry(root, width=40, font=("Arial", 12))
        self.entryText.grid(row=0, column=1, padx=10, pady=20, sticky='w')

        self.hash_type_label = tk.Label(root, text="Tipo de Hash:", font=("Arial", 14))
        self.hash_type_label.grid(row=1, column=0, padx=20, pady=20, sticky='w')

        self.hash_type_var = tk.StringVar()
        self.hash_type_var.set("sha224")
        self.hash_type_menu = tk.OptionMenu(root, self.hash_type_var, "sha224", "sha256" ,"sha384", "sha512", "sha3_224", "sha3_256", "sha3_384", "sha3_512")

        self.hash_type_menu.config(font=("Arial", 12))
        self.hash_type_menu.grid(row=1, column=1, padx=10, pady=20, sticky='w')

        self.result_label = tk.Label(root, text="Resultado:", font=("Arial", 14))
        self.result_label.grid(row=3, column=0, padx=20, pady=20, sticky='w')

        self.result_text = tk.Text(root, height=4, width=50, font=("Arial", 12))
        self.result_text.grid(row=3, column=1, columnspan=2, padx=10, pady=20, sticky='w')
        self.result_text.config(state="disabled", bg="light gray")

        self.return_button = tk.Button(root, text="Voltar", command=self.return_to_source_type_window, font=("Arial", 12))
        self.return_button.grid(row=4, column=2, padx=10, pady=20, sticky='w')

        if is_file == 'file':
            self.file_mode_app()
        else:
            self.input_mode_app()

    def input_mode_app(self):
        self.calculate_button = tk.Button(root, text="Calcular Hash", command=self.calculate_hash_input, font=("Arial", 12))
        self.calculate_button.grid(row=4, column=1, columnspan=2, pady=20, sticky='w')
        
    def file_mode_app(self):
        self.entryTextLabel = tk.Label(root, text="Caminho do Arquivo:", font=("Arial", 14))
        self.entryTextLabel.grid(row=0, column=0, padx=20, pady=20, sticky='w')

        self.browse_button = tk.Button(root, text="Procurar", command=self.browse_file, font=("Arial", 12))
        self.browse_button.grid(row=0, column=2, padx=10, pady=20, sticky='w')

        self.calculate_button = tk.Button(root, text="Calcular Hash", command=self.calculate_hash_file, font=("Arial", 12))
        self.calculate_button.grid(row=4, column=1, columnspan=3, pady=20, sticky='w')

    def return_to_source_type_window(self):
        clear_screen(root)
        ChooseSourceTypeWindow(root)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.entryText.delete(0, tk.END)
        self.entryText.insert(0, file_path)

    def calculate_hash_input(self):
        hash_type = self.hash_type_var.get()
        entryText = self.entryText.get()

        if not entryText:
            self.result_text.config(state="normal", bg="light gray")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Entre com o texto.")
            self.result_text.config(state="disabled", bg="light gray")
            return
        elif not limit_user_input(entryText):
            self.result_text.config(state="normal", bg="light gray")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Coloque uma entrada com menos de 5000 caracteres.")
            self.result_text.config(state="disabled", bg="light gray")
            return
        try:
            hash_result = hashlib.new(hash_type)
            hash_result.update(entryText.encode())
            self.result_text.config(state="normal", bg="light gray")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, hash_result.hexdigest())
            self.result_text.config(state="disabled", bg="light gray")
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Erro ao calcular o hash: {str(e)}")

    def calculate_hash_file(self):
        file_path = self.entryText.get()
        hash_type = self.hash_type_var.get()

        if not file_path:
            self.result_text.config(state="normal", bg="light gray")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Selecione um arquivo.")
            self.result_text.config(state="disabled", bg="light gray")
            return
        elif not check_file_size(self, file_path):
            return
        try:
            with open(file_path, "rb") as file:
                content = file.read()
                hash_result = hashlib.new(hash_type, content).hexdigest()
                self.result_text.config(state="normal", bg="light gray")
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, hash_result)
                self.result_text.config(state="disabled", bg="light gray")
        except FileNotFoundError:
            self.result_text.config(state="normal", bg="light gray")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Arquivo não encontrado.")
            self.result_text.config(state="disabled", bg="light gray")
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Erro ao calcular o hash: {str(e)}")

def clear_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

def centralize_screen(root):
    w = 800
    h = 400

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def check_file_size(self, file_path):
    try:
        file_size = os.stat(file_path).st_size / pow(1024, 2)
        if file_size < 48:
            return True
        else:
            self.result_text.config(state="normal")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Selecione um arquivo com menos de 48 MB.")
            self.result_text.config(state="disabled", bg="light gray")
            return False
    except FileNotFoundError:
        self.result_text.config(state="normal", bg="light gray")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Arquivo não encontrado.")
        self.result_text.config(state="disabled", bg="light gray")
    except OSError:
        self.result_text.config(state="normal", bg="light gray")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "OS error occurred.")
        self.result_text.config(state="disabled", bg="light gray")

def limit_user_input(entry):
    if len(entry) > 5000:
        return False
    return True

if __name__ == "__main__":
    root = tk.Tk()
    choose_source_type_window = ChooseSourceTypeWindow(root)
    root.mainloop()