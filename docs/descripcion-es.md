# Descripción del proyecto — Bybit Trading Bot

## Resumen

**Bybit Trading Bot — Paper & Live Mode** es un proyecto en Python para automatizar estrategias de trading con datos de mercado en tiempo real.

El objetivo principal no es prometer beneficios, sino demostrar una arquitectura segura con separación entre estrategia, control de riesgo, ejecución y registro de operaciones.

## Funciones principales

- modo paper trading;
- modo live opcional;
- datos de mercado por WebSocket;
- configuración para varios símbolos;
- capa de gestión de riesgo;
- registro de operaciones;
- alertas de monitorización;
- secretos almacenados mediante variables de entorno.

## Flujo

```text
Datos de Bybit
      ↓
Estrategia
      ↓
Gestor de riesgo
      ↓
Ejecutor paper o live
      ↓
Registro y alertas
```

## Seguridad

- paper trading por defecto;
- claves API solo en `.env` local;
- límites de posición;
- control de pérdidas;
- lista permitida de símbolos;
- revisión manual antes de activar live mode.

## Aviso

Este repositorio tiene fines educativos y de portafolio. No constituye asesoramiento financiero y no garantiza beneficios.
