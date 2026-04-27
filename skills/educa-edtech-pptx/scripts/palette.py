"""Paleta y tipografía oficial de Educa Edtech Group.

Importar desde cualquier script que genere una presentación del grupo
para evitar que se cuelen colores o fuentes off-brand.
"""

from pptx.dml.color import RGBColor


# --- Colores primarios ---------------------------------------------------
CARBON      = RGBColor(0x45, 0x45, 0x46)   # Títulos sobre blanco, fondos oscuros de sección
BLANCO      = RGBColor(0xFF, 0xFF, 0xFF)
NEGRO       = RGBColor(0x00, 0x00, 0x00)   # Barra lateral EDUCA EDTECH Group

# --- Grises de apoyo -----------------------------------------------------
GRIS_CLARO  = RGBColor(0xEB, 0xEB, 0xEB)   # Fondos de tarjetas, zebra de tabla
GRIS_CLARO2 = RGBColor(0xD5, 0xD5, 0xD5)   # Bandas, números decorativos tenues
GRIS_MEDIO  = RGBColor(0xBA, 0xBA, 0xBA)   # Texto secundario, separadores

# --- Azul corporativo ----------------------------------------------------
AZUL_EDUCA  = RGBColor(0x24, 0x4A, 0x80)   # Caja de índice, acentos estructurales

# --- Acentos para datos / gráficos --------------------------------------
ACCENT_DATOS = [
    RGBColor(0x2E, 0x7A, 0xBE),  # azul claro
    RGBColor(0x60, 0xBF, 0xB8),  # verde agua (positivo)
    RGBColor(0xE9, 0x6A, 0x73),  # coral (alerta)
    RGBColor(0x96, 0x30, 0x58),  # burdeos
]

# Hex en string, útil para matplotlib
ACCENT_DATOS_HEX = ["#2E7ABE", "#60BFB8", "#E96A73", "#963058"]
CARBON_HEX      = "#454546"
GRIS_MEDIO_HEX  = "#BABABA"
AZUL_EDUCA_HEX  = "#244A80"

# --- Tipografía ----------------------------------------------------------
FONT_TITLE     = "Rubik Medium"     # Portadas y titulares
FONT_SUBTITLE  = "Rubik Light"      # Subtítulos / eyebrow
FONT_BODY      = "Lato"             # Cuerpo de texto
FONT_NUMERO    = "Montserrat ExtraBold"  # Números gigantes decorativos

# Tamaños canónicos (en pt)
SIZE_PORTADA   = 80
SIZE_TITULO    = 60
SIZE_DESTACADO = 30
SIZE_SUBTITULO = 25
SIZE_BODY      = 20
SIZE_CAPTION   = 14
