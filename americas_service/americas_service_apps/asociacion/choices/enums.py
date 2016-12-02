# -*- coding: utf-8 -*-
E1 = "Terreno sin construir"
E2 = "Terreno con cerco perimetrico"
E3 = "Inmueble parcialmente construido"
E4 = "Inmueble construido - primera planta"
E5 = "Inmueble construido - segunda planta"
E6 = "Inmueble construido - más de dos plantas"

ESTADO_INMUEBLE_CHOICES = (
    (E1, "Terreno sin construir"),
    (E2, "Terreno con cerco perimetrico"),
    (E3, "Inmueble parcialmente construido"),
    (E4, "Inmueble construido - primera planta"),
    (E5, "Inmueble construido - segunda planta"),
    (E6, "Inmueble construido - más de dos plantas")
)

B1 = "Caja Arequipa"
B2 = "Caja Piura"
BANCO_CHOICES = (
    (B1, "Caja Arequipa"),
    (B2, "Caja Piura")
)

TC1 = "TC1"
TC2 = "TC2"

TIPO_CUENTA_CHOICES = (
    (TC1, "Cuenta de ahorros"),
    (TC2, "Cuenta corriente")
)
