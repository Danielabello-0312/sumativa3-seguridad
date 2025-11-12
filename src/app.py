"""
Ejemplo de aplicación Python para analizar
"""

def insecure_password_check(password):
    # Esto será detectado por bandit como inseguro
    if password == "admin123":
        return True
    return False

def main():
    print("Aplicación de ejemplo")
    # Código de ejemplo aquí

if __name__ == "__main__":
    main()