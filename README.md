Backend Métodos numéricos

Este proyecto de backend se basa en una arquitectura de microservicios utilizando Flask para resolver diversos problemas de métodos numéricos. Cada microservicio está diseñado para realizar cálculos específicos, como:

- Raíces de ecuaciones no lineales (método de bisección, Newton-Raphson, etc.)
- Sistemas de ecuaciones lineales (método de Gauss)
- Integración numérica (Regla del trapecio, Simpson, etc.)

Cada funcionalidad está expuesta como un endpoint RESTful, lo que facilita su uso y escalabilidad.

Características
- Microservicios modulares: Cada método numérico está implementado como un microservicio independiente.
- Escalabilidad: La arquitectura facilita la adición de nuevos métodos y la implementación en un entorno distribuido.
- APIs RESTful: Los endpoints están diseñados de manera estandarizada para facilitar el consumo de las APIs.

Despliegue con Docker

Este proyecto también está configurado para ser ejecutado en un contenedor Docker, lo que facilita su despliegue en cualquier entorno.