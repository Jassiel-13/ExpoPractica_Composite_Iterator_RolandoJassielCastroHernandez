# 🍽️ Patrón Compuesto + Iterador (GoF)
**Autor:** Rolando Jassiel Castro Hernández (N° 7)  
**Lenguaje:** Python  
**Materia:** Administración de Redes  

---

## 🧩 Descripción
Este proyecto implementa los patrones **Composite (Compuesto)** y **Iterator (Iterador)** para representar un **árbol genealógico** o estructura jerárquica, en este caso, adaptado a un **sistema de menú** con submenús y elementos individuales.

El patrón **Composite** permite tratar objetos individuales y composiciones de objetos de manera uniforme.  
El patrón **Iterator** proporciona una forma de recorrer los elementos del árbol sin exponer su estructura interna.

---

## 🎯 Contexto de Aplicación Real
En la vida real, este patrón se puede aplicar en sistemas donde existe una jerarquía de elementos que deben ser procesados o mostrados de forma recursiva:

- Árbol genealógico (familias y descendientes)  
- Estructura organizacional (departamentos y empleados)  
- Menús de aplicaciones, páginas web o restaurantes  
- Directorios y archivos en un sistema operativo  

---

## 📂 Estructura del Proyecto
```
CompositeIterator_RolandoJassielCastroHernandez/
│
├── src/
│ ├── component.py
│ ├── menu_item.py
│ ├── menu.py
│ ├── iterator.py
│ └── main.py
│
├── output_console.txt
├── LICENSE
└── README.md
```

---


---

## 🧱 Diagrama UML Simplificado
```text
        ┌────────────────────────┐
        │      Component (ABC)    │
        │ ─────────────────────── │
        │ + mostrar(nivel)        │
        │ + crear_iterador()      │
        └───────────┬────────────┘
                    │
      ┌─────────────┴─────────────┐
      │                           │
┌─────────────┐          ┌────────────────┐
│  MenuItem   │          │      Menu      │
│─────────────│          │────────────────│
│ - nombre    │          │ - nombre       │
│ - precio    │          │ - elementos[]  │
│─────────────│          │ + agregar()    │
│ + mostrar() │          │ + mostrar()    │
│ + crear_iterador()│    │ + crear_iterador() │
└─────────────┘          └────────────────┘
                            │
                            ▼
                 ┌────────────────────────┐
                 │   CompositeIterator     │
                 │────────────────────────│
                 │ + __next__()           │
                 │ + __iter__()           │
                 └────────────────────────┘
```

## 🧩 Código Principal
```
from src.menu import Menu
from src.menu_item import MenuItem

def main():
    menu_principal = Menu("Menú Principal")

    desayunos = Menu("Desayunos")
    comidas = Menu("Comidas")
    postres = Menu("Postres")

    desayunos.agregar(MenuItem("Hotcakes", 60))
    desayunos.agregar(MenuItem("Café", 25))

    comidas.agregar(MenuItem("Hamburguesa", 85))
    comidas.agregar(MenuItem("Refresco", 30))

    postres.agregar(MenuItem("Pastel de Chocolate", 70))
    postres.agregar(MenuItem("Helado", 50))

    menu_principal.agregar(desayunos)
    menu_principal.agregar(comidas)
    menu_principal.agregar(postres)

    print("🍽️ Estructura del Menú Compuesto")
    print("---------------------------------")
    menu_principal.mostrar()

    print("\n🔁 Recorriendo con el Iterador:")
    for item in menu_principal.crear_iterador():
        if isinstance(item, MenuItem):
            print(f"  - {item.nombre} (${item.precio})")

if __name__ == "__main__":
    main()
```
---

## 💻 Ejecución

Ejecuta el programa desde la raíz del proyecto con:
  python src/main.py


---

## 🧩 Ejemplo de Salida
🍽️ Estructura del Menú Compuesto
---------------------------------
> Menú Principal
  > Desayunos
    - Hotcakes - $60
    - Café - $25
  > Comidas
    - Hamburguesa - $85
    - Refresco - $30
  > Postres
    - Pastel de Chocolate - $70
    - Helado - $50

🔁 Recorriendo con el Iterador:
  - Hotcakes ($60)
  - Café ($25)
  - Hamburguesa ($85)
  - Refresco ($30)
  - Pastel de Chocolate ($70)
  - Helado ($50)


---

## ❌ Ejemplo de Mala Práctica

Un código sin patrones podría tener múltiples estructuras anidadas o condiciones repetitivas:
def mostrar_menu():
    print("Menú Principal")
    print("  Desayunos")
    print("    Hotcakes - $60")
    print("    Café - $25")
    print("  Comidas")
    print("    Hamburguesa - $85")
    print("    Refresco - $30")
    print("  Postres")
    print("    Pastel de Chocolate - $70")
    print("    Helado - $50")
    
💀 Problema: difícil de mantener o escalar si se agregan nuevas categorías o submenús.


---

## ✅ Refactorización Aplicando Composite + Iterator

Con el patrón Composite, cada elemento puede ser tratado de forma uniforme.
Con Iterator, se recorre todo el árbol sin importar su profundidad.

Beneficios:

Código más limpio y extensible

Se pueden agregar niveles ilimitados de jerarquía

Facilita recorrer todos los elementos con un único iterador


---

## 🧠 Relación con los Principios SOLID
Principio	Relación
S (Responsabilidad Única)	Cada clase tiene una única función: mostrar o iterar.
O (Abierto/Cerrado)	Se pueden agregar nuevos tipos de menús sin modificar código existente.
L (Sustitución de Liskov)	Los objetos MenuItem y Menu pueden usarse de forma intercambiable.
I (Segregación de Interfaces)	Las clases implementan solo los métodos que necesitan.
D (Inversión de Dependencias)	El cliente depende de abstracciones (Component), no de clases concretas.
