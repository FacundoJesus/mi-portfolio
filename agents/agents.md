# Portfolio Web de Facundo Citera

Este documento establece las reglas, stack, y convenciones para el desarrollo y mantenimiento del proyecto "Portfolio Web".

## Stack
- **HTML5:** Estructura de las páginas.
- **CSS3:** Estilos personalizados (`styles.css`).
- **JavaScript (Vanilla):** Lógica del lado del cliente, animaciones (efecto de máquina de escribir) e integración de servicios.
- **Bootstrap 5.3:** Framework CSS principal para layout, grillas (`row`, `col`), navegación (`navbar`) y utilidades.
- **Bibliotecas y APIs Externas:**
  - **EmailJS:** Para el envío de correos desde el formulario de contacto sin necesidad de backend.
  - **FontAwesome 6 / Material Symbols / Tabler Icons:** Para iconos a lo largo del sitio (redes sociales, navegación, etc.).
  - **Google Fonts:** Fuentes utilizadas (`Abel`, `Arvo`, `Climate Crisis`, `Lato`, `Sevillana`, `Ubuntu`).
  - **Animate.css:** (Aunque se ven clases como `animate__animated`, revisar si está importada o se usa un custom CSS).

## Comandos
Al ser un proyecto estático sin un gestor de paquetes (como npm o yarn), no hay scripts de build o dependencias de Node.js configuradas.
- **Desarrollo Local:** Para visualizar los cambios, simplemente abre cualquier archivo `.html` (ej. `index.html`) en tu navegador web. Alternativamente, se recomienda usar la extensión "Live Server" de VSCode o ejecutar un servidor estático básico (ej. `npx http-server` o `python -m http.server`) en la raíz del proyecto.

## Estructura del proyecto
El proyecto sigue una estructura plana en la raíz para los archivos HTML y carpetas dedicadas para recursos:

```
portafolio_web/
├── .agents/                 # Reglas y configuración para agentes de IA
├── imgs/                    # Imágenes estáticas y logos organizados en subcarpetas (ej. fotos, logos)
├── proyectos_arq/           # Archivos y recursos específicos de los proyectos de arquitectura
├── styles.css               # Hoja de estilos global y personalizada
└── *.html                   # Páginas estáticas (index.html, contacto.html, cv_*.html, certificaciones_*.html, etc.)
```

## Convenciones
1. **Idioma de Desarrollo:** El contenido y las clases personalizadas suelen usar español (ej. `sobre-mi`, `presentacion`, `tamaño-estilo-fuente`).
2. **Uso de Bootstrap:** Priorizar las clases utilitarias y componentes de Bootstrap (como el Grid System) para el diseño responsivo antes de crear CSS personalizado.
3. **Estilos Custom:** El CSS personalizado (`styles.css`) debe usarse para ajustar detalles finos, animaciones propias o componentes que Bootstrap no cubra.
4. **Iconografía:** Se utilizan múltiples fuentes de iconos. Se prefieren SVG inline o clases de FontAwesome para mantener consistencia.
5. **Navegación:** El menú (navbar) debe ser consistente en todos los archivos `.html` principales, ya que no se utiliza un motor de plantillas (templating). Cualquier cambio en el menú general debe replicarse en todos los archivos HTML aplicables.

## No hagas
- **No añadir frameworks pesados de JavaScript:** Evitar añadir React, Vue, Angular o dependencias complejas. Mantener el proyecto como Vanilla JS + HTML estático.
- **No romper la estructura del Navbar:** Al no tener componentes reutilizables (sin un framework JS o PHP), evita hacer cambios masivos en el navbar de un solo archivo sin considerar que debe modificarse en todos los demás HTML.
- **No abusar de estilos inline:** Evita el uso del atributo `style` dentro de las etiquetas HTML a menos que sea estrictamente necesario (ej. dinamismo por JS). Usa `styles.css` o las utilidades de Bootstrap.
- **No remover referencias de EmailJS:** El formulario de contacto en `contacto.html` y la página principal dependen de EmailJS. No modifiques las llaves (`jfPgseaTi6W-BrtvE`, `service_kwdtme8`, etc.) a menos que hayan sido rotadas.

## Flujo de trabajo
1. **Modificaciones Visuales:** Editar el archivo `.html` correspondiente o `styles.css`. Comprobar siempre la responsividad (vista móvil, tablet y escritorio) gracias a Bootstrap.
2. **Crear nuevas secciones/páginas:** Duplicar una página existente (para heredar el `<head>` y el `<nav>`) y limpiar el contenido del `<body>`.
3. **Manejo de Imágenes:** Optimizar imágenes antes de subirlas a la carpeta `imgs` para no ralentizar la carga del sitio.
4. **Despliegue (Deploy):** Al ser un sitio estático puro, puede ser desplegado fácilmente haciendo push a una rama principal en servicios como GitHub Pages, Vercel, Netlify o un hosting tradicional.

## Documentación
- [Documentación de Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [EmailJS SDK](https://www.emailjs.com/docs/)
- [Tabler Icons](https://tabler-icons.io/)
- El portafolio está estructurado en torno a las áreas de Arquitectura, Programación e Inglés, organizando las certificaciones, currículums y proyectos de forma categorizada.
