# sistema_control_des_seg
Criterios de Aceptación Funcionales:

[ ] El botón debe estar visible y descargar un PDF.

🛡️ Criterios de Aceptación de Seguridad:

[ ] Seguridad: La URL de descarga NO debe contener el RUT del alumno en texto

plano.

[ ] Seguridad: El backend debe validar el Token de Sesión JWT del usuario antes de

generar el documento (Autorización).

[ ] Seguridad: La librería de generación PDF debe estar libre de vulnerabilidades (CVEs).