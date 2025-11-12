#!/usr/bin/env python3
"""
Script de escaneo de seguridad para DevSecOps
"""

import subprocess
import sys
import os

def install_dependencies():
    """Instala bandit si no está disponible"""
    try:
        import bandit
        print("✅ Bandit ya está instalado")
        return True
    except ImportError:
        print("📦 Bandit no encontrado. Instalando...")
        try:
            subprocess.run([
                sys.executable, "-m", "pip", "install", "bandit"
            ], check=True, capture_output=True)
            print("✅ Bandit instalado correctamente")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error instalando bandit: {e}")
            return False

def run_security_scan():
    """Ejecuta el análisis de seguridad con bandit"""
    print("🔍 Ejecutando análisis de seguridad con Bandit...")
    
    try:
        result = subprocess.run(
            ["bandit", "-r", "src", "-f", "txt"],
            capture_output=True,
            text=True
        )
        
        print("=" * 50)
        print("📊 RESULTADO DEL ESCANEO DE SEGURIDAD:")
        print("=" * 50)
        print(result.stdout)
        
        if result.stderr:
            print("⚠️ ADVERTENCIAS:")
            print(result.stderr)
        
        if result.returncode != 0:
            print("❌ Se encontraron problemas de seguridad")
        else:
            print("✅ No se encontraron vulnerabilidades")
            
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Error ejecutando bandit: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Iniciando pipeline de seguridad...")
    
    if install_dependencies():
        success = run_security_scan()
        if success:
            print("🎉 Análisis de seguridad completado EXITOSAMENTE")
        else:
            print("💥 Análisis de seguridad encontró problemas")
            sys.exit(1)  # Sale con error para que Jenkins lo detecte
    else:
        print("💥 No se pudo instalar bandit")
        sys.exit(1)