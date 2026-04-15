# App Biblioteca (Base)

Documentacion basica del modulo `app` para trabajo colaborativo.

## Requisitos

- Python 3.10+

## Como ejecutar

Desde la raiz del repositorio:

```bash
python app/main.py
```

## Estructura actual

```text
app/
	main.py          # Punto de entrada principal
	utils.py         # Funciones de apoyo compartidas
	menu/
		index.py       # Menu por tipo de usuario (alumno/admin)
```

## Flujo base

1. `main.py` muestra menu inicial (iniciar sesion / registrarse).
2. Si se elige iniciar sesion, se llama `menu.index.menu("alumno")`.
3. `menu()` mantiene el ciclo de opciones hasta seleccionar `5. Salir`.

## Convenciones para colaborar

- No borrar ni cambiar firmas publicas sin acuerdo previo:
	- `main()` en `main.py`
	- `menu(userType="alumno")` en `menu/index.py`
	- `esOpcion(...)` en `utils.py`
- Mantener opciones de menu como `str` (porque `input()` retorna texto).
- Agregar nuevas funcionalidades en modulos separados por dominio (por ejemplo: `libros/`, `salas/`, `usuarios/`) para reducir conflictos de merge.
- Si agregas una opcion de menu, actualizar:
	- lista de opciones
	- impresion de menu
	- comportamiento de la opcion

## Checklist antes de subir cambios

1. Ejecutar `python app/main.py` sin errores.
2. Verificar al menos un flujo valido y una opcion invalida.
3. Confirmar que los imports siguen funcionando desde la raiz del repo.
4. Actualizar esta documentacion si cambias flujo o estructura.
