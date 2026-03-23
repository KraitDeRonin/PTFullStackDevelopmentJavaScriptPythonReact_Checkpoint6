class Usuario:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

nuevo_usuario = Usuario("admin_dev", "P@ssw0rd2026")

print(f"Objeto creado exitosamente.")
print(f"Nombre de usuario: {nuevo_usuario.username}")
print(f"Contraseña almacenada: {nuevo_usuario.password}")