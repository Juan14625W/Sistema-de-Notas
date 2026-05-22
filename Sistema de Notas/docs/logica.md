# logica.py

Resumen

`Logica` contiene las reglas del dominio: validación de correos, validación de notas y fórmulas para calcular las notas por corte y la definitiva.

Métodos y reglas

- `validar_correo(correo)` -> valida que el correo no contenga caracteres o patrones sospechosos y que termine en `@uniautonoma.edu.co`.
  - Reglas observadas: bloquea si el tercer carácter es `*`, si el segundo carácter es `m`, o si contiene `+`, `=` ó `&`.
  - Retorna `(bool, mensaje)`.

- `validar_nota(nota)` -> intenta convertir `nota` a `float` y valida que esté entre `0.0` y `5.0`.
  - Retorna `(True, float)` en caso válido o `(False, mensaje)` en caso de error.

- `calcular_nota_corte(trabajos, quices, parcial)` -> aplica ponderaciones 30% trabajos, 30% quices, 40% parcial.

- `calcular_definitiva(corte1, corte2, final)` -> pondera cortes: 35% corte1, 35% corte2, 30% final.

- `verificar_aprobado(definitiva)` -> devuelve `"Aprobado"` si la definitiva es mayor a 3.5, sino `"Reprovado"`.

Sugerencias

- Normalizar mensajes y errores para internacionalización o consistencia.
- Añadir pruebas unitarias para casos límite (p. ej. 0.0, 5.0, 3.5).
- Revisar las reglas de `validar_correo` si deben ser más estrictas o flexibles.
