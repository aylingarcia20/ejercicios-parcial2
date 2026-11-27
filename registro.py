from supabase import create_client, Client


URL = "PEGA_AQUI_TU_PROJECT_URL"
KEY = "PEGA_AQUI_TU_ANON_PUBLIC_KEY"

supabase: Client = create_client(URL, KEY)

print("=== SISTEMA DE REGISTRO DE USUARIOS")
correo = input("ingresa tu correo electronico")
contrasena 0 input("Crea una contraseña (minimo 6 caracteres):")


try:
    respuesta = supabase.auth.sign_up([
        "email": correo,
        