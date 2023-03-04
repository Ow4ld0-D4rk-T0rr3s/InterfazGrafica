import tkinter as tk
import csv

class RegistroEstudianteProfesor:
    def __init__(self, master):
        self.master = master
        self.master.iconbitmap("home.ico")
        self.master.title("..::Registro de estudiantes y profesores::..")
        self.init_ui()

    def init_ui(self):
        self.titulo = tk.Label(self.master, text="...:::Bienvenidos al Registro de Datos:::...", font=("Comic Sans MS", 12))
        self.titulo.pack(pady=10)
        
        self.btn_estudiante = tk.Button(
        self.master, text="Estudiantes", padx=15, pady=15, command=self.abrir_ventana_estudiante
        )
        self.btn_profesor = tk.Button(
        self.master, text="Profesores", padx=15, pady=15, command=self.abrir_ventana_profesor
        )
        
        self.btn_estudiante.pack(side=tk.LEFT, padx=10, pady=10)
        self.btn_profesor.pack(side=tk.RIGHT, padx=10, pady=10)
        
    def abrir_ventana_estudiante(self):
        self.ventana_estudiante = tk.Toplevel(self.master)
        self.ventana_estudiante.title("Registro de estudiante")
    
        self.nombre_estudiante = tk.StringVar()
        self.boleta = tk.StringVar()
        self.grupo = tk.StringVar()

        tk.Label(self.ventana_estudiante, text="Nombre:", fg="red").grid(
            row=0, column=0, padx=10, pady=10
        )
        tk.Entry(self.ventana_estudiante, textvariable=self.nombre_estudiante).grid(
            row=0, column=1, padx=10, pady=10
        )
        
        tk.Label(self.ventana_estudiante, text="Boleta:", fg="red").grid(
            row=1, column=0, padx=10, pady=10
        )
        tk.Entry(self.ventana_estudiante, textvariable=self.boleta).grid(
            row=1, column=1, padx=10, pady=10
        )

        tk.Label(self.ventana_estudiante, text="Grupo:", fg="red").grid(
            row=2, column=0, padx=10, pady=10
        )
        tk.Entry(self.ventana_estudiante, textvariable=self.grupo).grid(
            row=2, column=1, padx=10, pady=10
        )

        tk.Button(
        self.ventana_estudiante, text="Guardar", command=self.guardar_datos_alumno).grid(
            row=4, column=0, padx=10, pady=10)
        
        tk.Button(
        self.ventana_estudiante, text="Mostrar", command=self.mostrar_datos_alumno).grid(
            row=4, column=1, padx=10, pady=10)
        
        tk.Button(
        self.ventana_estudiante, text="Limpaiar", command=self.borrar_lista_estudiante).grid(
            row=4, column=2, padx=10, pady=10)
        
        self.datos_listbox = tk.Listbox(self.ventana_estudiante)
        self.datos_listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
            
        self.scrollbar = tk.Scrollbar(self.ventana_estudiante, orient=tk.VERTICAL, command=self.datos_listbox.yview)
        self.scrollbar.grid(row=6, column=2, sticky=tk.NS)
        self.datos_listbox.configure(yscrollcommand=self.scrollbar.set)

        
    def abrir_ventana_profesor(self):
        self.ventana_profesor = tk.Toplevel(self.master)
        self.ventana_profesor.title("Registro de profesor")

        self.nombre_profesor = tk.StringVar()
        self.materia = tk.StringVar()
        self.grupo_asignado = tk.StringVar()

        tk.Label(self.ventana_profesor, text="Profesor:", fg="blue").grid(
            row=0, column=0, padx=10, pady=10
        )
        tk.Entry(self.ventana_profesor, textvariable=self.nombre_profesor).grid(
            row=0, column=1, padx=10, pady=10
        )

        tk.Label(self.ventana_profesor, text="Materia:", fg="blue").grid(
            row=1, column=0, padx=10, pady=10
        )
        tk.Entry(self.ventana_profesor, textvariable=self.materia).grid(
            row=1, column=1, padx=10, pady=10
        )
        tk.Label(self.ventana_profesor, text="Grupo Asignado:", fg="blue").grid(
        row=2, column=0, padx=10, pady=10
         )
        tk.Entry(self.ventana_profesor, textvariable=self.grupo_asignado).grid(
        row=2, column=1, padx=10, pady=10
         )
        tk.Button(
        self.ventana_profesor, text="Guardar", command=self.guardar_datos_profesor).grid(
            row=4, column=0, padx=10, pady=10
        )
        tk.Button(self.ventana_profesor, text="Mostrar", command=self.mostrar_datos_profesor).grid(
            row=4, column=1, padx=10, pady=10
        )
        tk.Button(self.ventana_profesor, text="Limpaiar", command=self.borrar_lista_profesor).grid(
            row=4, column=2, padx=10, pady=10)

        self.datos_listbox = tk.Listbox(self.ventana_profesor)
        self.datos_listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        
        self.scrollbar = tk.Scrollbar(self.ventana_profesor, orient=tk.VERTICAL, command=self.datos_listbox.yview)
        self.scrollbar.grid(row=6, column=2, sticky=tk.NS)
        self.datos_listbox.configure(yscrollcommand=self.scrollbar.set)

    def guardar_datos_alumno(self):
        nombre = self.nombre_estudiante.get()
        boleta = self.boleta.get()
        grupo = self.grupo.get()
        
        with open("alumnos.csv", "a", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow([nombre, boleta, grupo])
            
        self.nombre_estudiante.delete(0, tk.END)
        self.boleta.delete(0, tk.END)
        self.grupo.delete(0, tk.END)

    def mostrar_datos_alumno(self):
        self.datos_listbox.delete(0, tk.END)
        
        with open("alumnos.csv", "r") as archivo:
            lector_csv = csv.reader(archivo)
            
            for linea in lector_csv:
                self.datos_listbox.insert(tk.END, linea)   
                     
    def borrar_lista_estudiante(self):
        self.datos_listbox.delete(0, tk.END)          
              
    def guardar_datos_profesor(self):
        nombre_profesor = self.nombre_profesor.get()
        materia = self.materia.get()
        grupo_asignado = self.grupo_asignado.get()
        
        with open("profesor.csv", "a", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow([nombre_profesor, materia, grupo_asignado])
        
        self.nombre_profesor.delete(0, tk.END)
        self.materia.delete(0, tk.END)
        self.grupo_asignado.delete(0, tk.END)

    def mostrar_datos_profesor(self):
        self.datos_listbox.delete(0, tk.END)
        
        with open("profesor.csv", "r") as archivo:
            lector_csv = csv.reader(archivo)
            
            for linea in lector_csv:
                self.datos_listbox.insert(tk.END, linea)  
                 
    def borrar_lista_profesor(self):
        self.datos_listbox.delete(0, tk.END)             

if __name__ == "__main__":
    root = tk.Tk()

    # Set window position and size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 600
    window_height = 400
    window_x = int((screen_width - window_width) / 2)
    window_y = int((screen_height - window_height) / 2)

    root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
    interface = RegistroEstudianteProfesor(root)
    root.mainloop()

