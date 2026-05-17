# Scuba Cat - Hand Tracking Animation

Aplicación de visión por computadora en tiempo real que usa la webcam, detecta hasta dos manos con MediaPipe y abre ventanas animadas cuando hay movimiento.

## Qué hace

- Detecta hasta dos manos con MediaPipe.
- Usa la posición horizontal de la mano para activar la experiencia.
- Abre y cierra dos ventanas de GIF animado cuando las dos manos están visibles y activas.
- Reproduce un sonido mientras las ventanas están abiertas.
- Cierra todo con la tecla `q`.

## Cómo funciona

- `main.py` controla el bucle principal: cámara, detección, activación de ventanas, reproducción de GIF y audio.
- `src/detector.py` encapsula MediaPipe Hands y devuelve los landmarks detectados.
- `src/overlay_utils.py` carga los GIF, los escala y los convierte a frames listos para OpenCV.
- `assets/` contiene los recursos obligatorios: los dos GIF y el archivo de audio.

## Tecnologías usadas

- Python 3.12
- MediaPipe 0.10.13
- OpenCV 4.13.0.92
- Pillow 12.2.0
- numpy 2.4.5
- pygame 2.6.1

## Requisitos recomendados

Para este proyecto conviene usar las versiones fijadas en `requirements.txt`. Como es una app pequeña y para compartir con amigos, fijar versiones da más estabilidad y evita que una actualización de MediaPipe, OpenCV o pygame rompa la ejecución. Si luego quieres actualizar dependencias, hazlo de forma controlada y vuelve a probar la app.

## Instalación paso a paso en macOS

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd scuba-cat-hand-tracker
```

### 2. Instalar Python 3.12

Si no lo tienes instalado, puedes usar Homebrew:

```bash
brew install python@3.12
```

Verifica la instalación:

```bash
python3 --version
```

### 3. Crear un entorno virtual

```bash
python3 -m venv .venv
```

### 4. Activar el entorno virtual

```bash
source .venv/bin/activate
```

### 5. Actualizar pip

```bash
python -m pip install --upgrade pip
```

### 6. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 7. Dar permisos en macOS

La primera vez, macOS puede pedir permisos para usar la cámara y el audio. Si la app no ve la webcam o no reproduce sonido, revisa:

- `Ajustes del sistema > Privacidad y seguridad > Cámara`
- `Ajustes del sistema > Privacidad y seguridad > Micrófono` o permisos del terminal, según el sistema

### 8. Ejecutar la aplicación

```bash
python main.py
```

## Uso

1. Abre la app con la cámara conectada.
2. Pon ambas manos frente a la webcam para activar las ventanas.
3. Mientras las ventanas estén visibles, el sonido se reproduce en bucle.
4. Si las dos manos dejan de detectarse o no hay activación, las ventanas se cierran y el sonido se detiene.
5. Presiona `q` para salir.

## Estructura del proyecto

```text
main.py
README.md
requirements.txt
assets/
   cat_animation.gif
   nick_animation.gif
   scubbaaa.mp3
src/
   __init__.py
   detector.py
   overlay_utils.py
```

## Archivos importantes

- [main.py](main.py): bucle principal y ciclo de vida de la app.
- [src/detector.py](src/detector.py): wrapper de MediaPipe Hands.
- [src/overlay_utils.py](src/overlay_utils.py): carga y conversión de GIF.
- [requirements.txt](requirements.txt): dependencias fijadas a versiones probadas.

## Comportamiento actual

- La cámara usa el dispositivo `0`.
- La imagen se espeja para interacción tipo espejo.
- La app solo activa los GIF si detecta 2 manos.
- Cada GIF se reproduce por tiempo propio para verse más fluido.
- El sonido `assets/scubbaaa.mp3` arranca cuando se abren las ventanas y se detiene al cerrarse.

## Solución de problemas

### No abre la cámara

- Revisa que otra app no esté usando la webcam.
- Prueba cambiar el dispositivo de cámara en `cv2.VideoCapture(0)`.

### MediaPipe falla al importar

- Verifica que estés usando Python 3.12.
- Reinstala las dependencias con el entorno virtual activo.

### Los GIF no aparecen

- Confirma que existen `assets/cat_animation.gif` y `assets/nick_animation.gif`.

### No suena el audio

- Confirma que existe `assets/scubbaaa.mp3`.
- Revisa que `pygame` esté instalado correctamente.

## Notas de desarrollo

- Este proyecto está pensado para uso divertido y compartido, no como producto serio.
- Se prioriza simplicidad y experiencia visual sobre arquitectura compleja.
- Si cambias la sensibilidad de manos, revisa el umbral de movimiento y el tiempo de activación en `main.py`.

## Próximas ideas

- Añadir gestos reales en lugar de solo movimiento horizontal.
- Permitir elegir personajes o sonidos desde teclado.
- Hacer configurable la cámara, el umbral de movimiento y la velocidad de los GIF.
- Soportar más personajes cargados desde `assets/`.
