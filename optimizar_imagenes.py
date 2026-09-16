import os
from pathlib import Path
from PIL import Image, ImageOps

# Configuración de optimización
DIRECTORIO_IMAGENES = Path("imgs")
MAX_WIDTH = 1920        # Ancho máximo permitido (Full HD)
MAX_HEIGHT = 1920       # Alto máximo permitido
CALIDAD_JPEG = 80       # Calidad de compresión (75-82 es el estándar óptimo web)
CALIDAD_WEBP = 80

EXTENSIONES_VALIDAS = {".jpg", ".jpeg", ".png"}

def obtener_tamano_legible(bytes_size):
    """Devuelve el tamaño en MB formateado."""
    return f"{bytes_size / (1024 * 1024):.2f} MB"

def optimizar_imagen(ruta_archivo):
    """
    Optimiza una imagen sobreescribiéndola con una versión redimensionada y comprimida.
    Mantiene la extensión original (.jpg, .jpeg, .png).
    """
    tamano_original = os.path.getsize(ruta_archivo)
    extension = ruta_archivo.suffix.lower()

    try:
        with Image.open(ruta_archivo) as img:
            # Corregir orientación según metadatos EXIF si existen
            img = ImageOps.exif_transpose(img)

            # Redimensionar si supera las dimensiones máximas
            img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.Resampling.LANCZOS)

            # Guardar temporalmente para comparar tamaño
            ruta_temp = ruta_archivo.with_suffix(".tmp" + extension)

            if extension in [".jpg", ".jpeg"]:
                # Convertir a RGB si es necesario (evita error con imágenes CMYK o RGBA en JPEG)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                img.save(ruta_temp, "JPEG", quality=CALIDAD_JPEG, optimize=True, progressive=True)

            elif extension == ".png":
                # Optimización para PNG
                if img.mode == "RGBA":
                    img.save(ruta_temp, "PNG", optimize=True)
                else:
                    img.save(ruta_temp, "PNG", optimize=True)

            tamano_nuevo = os.path.getsize(ruta_temp)

            # Solo reemplazar si el archivo resultante es efectivamente más liviano
            if tamano_nuevo < tamano_original:
                os.replace(ruta_temp, ruta_archivo)
                ahorro = tamano_original - tamano_nuevo
                return tamano_original, tamano_nuevo, ahorro
            else:
                # Si por alguna razón comprimir no redujo tamaño, descartar archivo temporal
                if os.path.exists(ruta_temp):
                    os.remove(ruta_temp)
                return tamano_original, tamano_original, 0

    except Exception as e:
        print(f"⚠️ Error procesando {ruta_archivo.name}: {e}")
        return tamano_original, tamano_original, 0

def main():
    if not DIRECTORIO_IMAGENES.exists():
        print(f"❌ No se encontró el directorio: {DIRECTORIO_IMAGENES}")
        return

    print("=" * 60)
    print("🚀 INICIANDO OPTIMIZACIÓN DE IMÁGENES (Camino A)")
    print(f"Directorio: {DIRECTORIO_IMAGENES.resolve()}")
    print(f"Dimensión máxima: {MAX_WIDTH}x{MAX_HEIGHT} px")
    print(f"Calidad JPEG: {CALIDAD_JPEG}%")
    print("=" * 60)

    archivos_procesar = [
        p for p in DIRECTORIO_IMAGENES.rglob("*")
        if p.is_file() and p.suffix.lower() in EXTENSIONES_VALIDAS
    ]

    total_archivos = len(archivos_procesar)
    print(f"Se encontraron {total_archivos} imágenes a revisar.\n")

    peso_total_inicial = 0
    peso_total_final = 0
    optimizadas_count = 0

    for i, archivo in enumerate(archivos_procesar, start=1):
        original, final, ahorro = optimizar_imagen(archivo)
        peso_total_inicial += original
        peso_total_final += final

        if ahorro > 0:
            optimizadas_count += 1
            porcentaje = ((original - final) / original) * 100
            print(f"[{i}/{total_archivos}] ✅ {archivo.name}: {obtener_tamano_legible(original)} -> {obtener_tamano_legible(final)} (-{porcentaje:.1f}%)")
        else:
            print(f"[{i}/{total_archivos}] ⏭️  {archivo.name}: ya optimizada o sin cambios")

    ahorro_total = peso_total_inicial - peso_total_final
    porcentaje_total = ((ahorro_total / peso_total_inicial) * 100) if peso_total_inicial > 0 else 0

    print("\n" + "=" * 60)
    print("✨ OPTIMIZACIÓN COMPLETADA")
    print("=" * 60)
    print(f"Archivos procesados: {total_archivos}")
    print(f"Archivos reducidos:   {optimizadas_count}")
    print(f"Peso inicial total:   {obtener_tamano_legible(peso_total_inicial)}")
    print(f"Peso final total:     {obtener_tamano_legible(peso_total_final)}")
    print(f"Espacio ahorrado:     {obtener_tamano_legible(ahorro_total)} (-{porcentaje_total:.2f}%)")
    print("=" * 60)
    print("💡 Tus archivos HTML y CSS permanecen 100% intactos.")

if __name__ == "__main__":
    main()
