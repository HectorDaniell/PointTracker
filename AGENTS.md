# Guía Del Proyecto

## Resumen
- Este repositorio es una app pequeña de visión por computadora en tiempo real que usa la webcam, detecta hasta dos manos con MediaPipe y abre ventanas animadas con OpenCV cuando detecta movimiento.
- La experiencia actual está centrada en dos personajes: `assets/cat_animation.gif` y `assets/nick_animation.gif`. Ambos GIF se cargan al iniciar y avanzan frames cuando cambia la posición horizontal de la mano.
- Trátalo como un script de escritorio de usuario único. No está organizado como librería, paquete reutilizable ni servicio.

## Ejecución Y Validación
- Crea y activa un entorno virtual antes de instalar dependencias.
- Instala dependencias con `python -m pip install -r requirements.txt`.
- Ejecuta la app con `python main.py`.
- La validación principal en este repositorio es manual: comprobar que abre la webcam, que aparece la ventana `Minha Camera`, que las ventanas animadas reaccionan al movimiento de la mano y que `q` cierra la app sin dejar ventanas abiertas.
- No hay suite de tests, linter ni formatter configurados.

## Arquitectura
- `main.py` controla todo el ciclo principal: captura de cámara, espejo horizontal, detección de movimiento, avance de frames, tiempo de inactividad y ciclo de vida de ventanas OpenCV.
- `src/detector.py` encapsula `mediapipe.solutions.hands` en `HandDetector` y expone detección de manos y dibujo opcional de landmarks.
- `src/overlay_utils.py` procesa los GIF una sola vez al inicio y los convierte en arrays listos para OpenCV.
- `assets/` contiene recursos obligatorios de ejecución. Si faltan esos archivos, la app falla al iniciar.

## Flujo Actual De La App
- Se carga la webcam desde el dispositivo `0`.
- Se espeja la imagen con `cv2.flip(img, 1)` para interacción tipo espejo.
- Se detectan hasta dos manos y se usa la landmark `0` de cada mano como referencia de movimiento horizontal.
- Si el cambio en `x` supera `10` píxeles, se considera movimiento.
- La mano en índice `0` avanza de a `1` frame y la mano en índice `1` avanza de a `2` frames.
- Si hubo movimiento en los últimos `0.5` segundos, se muestran ambas ventanas animadas; si no, se destruyen.

## Convenciones Para Cambios
- Haz cambios pequeños y directos. La mayor parte del comportamiento está en línea dentro de `main.py`.
- No introduzcas abstracciones nuevas salvo que el problema realmente lo pida. Este proyecto todavía es corto y el costo de sobrediseñar supera el beneficio.
- Conserva el modelo de interacción actual a menos que la tarea indique lo contrario: máximo dos manos, assets hardcodeados, cámara espejada y salida con `q`.
- Si cambias sensibilidad o comportamiento, toca el umbral de movimiento y el timeout de inactividad con intención clara. Hoy el sistema depende de `abs(curr_x - prev_x_positions[i]) > 10` y de un timeout global de `0.5` segundos.
- Prefiere agregar validaciones explícitas para fallos de webcam, assets o imports antes que esconder el problema con `try/except` amplios.

## Depuración Rápida
- Si falla el arranque, revisa primero que existan `assets/cat_animation.gif` y `assets/nick_animation.gif`.
- Si falla la cámara, revisa `cv2.VideoCapture(0)` y no asumas que el dispositivo correcto siempre es `0`.
- Si MediaPipe falla al importar o cambia su API, valida primero el entorno con `python -c "import mediapipe as mp; print(mp.solutions.hands)"` antes de editar `src/detector.py`.
- Si la app abre pero no anima, inspecciona el cálculo de `curr_x`, `prev_x_positions` y el umbral de `10` píxeles en `main.py`.
- Si las ventanas aparecen y desaparecen de forma inesperada, revisa `unified_last_move_time`, porque hoy ambas animaciones dependen de un solo temporizador global.

## Notas De Entorno
- El README está incompleto y puede quedar desactualizado respecto del entorno que realmente funciona. Antes de cambiar instrucciones de setup, valida contra el código y el entorno instalable actual.
- La compatibilidad de MediaPipe en Windows es sensible a la versión de Python y del wheel disponible. Si reaparece un error con `mp.solutions`, verifica primero la versión instalada de `mediapipe`.
- La app asume entorno gráfico de escritorio con capacidad para abrir ventanas OpenCV.

## Posibles Direcciones De Evolución
- Reconocimiento de gestos reales en lugar de depender solo del movimiento horizontal.
- Configuración externa para umbrales, GIF, escalas y cámara.
- Validaciones de arranque más claras para assets, webcam y dependencias.
- Separar la lógica de movimiento y animación de `main.py` si el proyecto crece.

## Referencias Útiles
- Ver [README.md](README.md) para la descripción general del proyecto y su intención funcional.