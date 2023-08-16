# Importamos las librerias
from deepface import DeepFace
import cv2
import mediapipe as mp


# Declaramos la detección de rostros
detros = mp.solutions.face_detection
rostros = detros.FaceDetection(min_detection_confidence= 0.8, model_selection=0)

# Dibujo
dibujorostro = mp.solutions.drawing_utils

# Realizamos VideoCaptura
cap = cv2.VideoCapture(0)


# Empezamos
while True:
    # Leemos los fotogramas
    ret, frame = cap.read()

    # Corrección de color de la camara
    rgb = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Procesamos
    resrostros = rostros.process(rgb)

    # Deteccion
    if resrostros.detections is not None:
        # Registramos
        for rostro in resrostros.detections:
            # Extraemos información de ubicación
            al, an, c = frame.shape
            box = rostro.location_data.relative_bounding_box
            xi, yi, w, h = int(box.xmin * an), int(box.ymin * al), int(box.width * an), int(box.height * al)
            xf, yf = xi + w, yi + h

            # Informacion
            info = DeepFace.analyze(rgb, actions=['age', 'gender', 'race', 'emotion'], enforce_detection=False)

            # Edad
            edad = info['age']

            # Emociones
            emociones = info['dominant_emotion']


            # Race
            race = info['dominant_race']

            # Genero
            gen = info['gender']
            print(str(gen) + " de " + str(edad) + " años de edad, con estado de animo " + str(emociones) + " de color de piel " + str(race))

            # Traducimos
            if gen == 'Man':
                gen = 'Hombre'

                # Emociones
                if emociones == 'angry':
                    emociones = 'enojado'
                if emociones == 'disgust':
                    emociones = 'disgustado'
                if emociones == 'fear':
                    emociones = 'miedoso'
                if emociones == 'happy':
                    emociones = 'feliz'
                if emociones == 'sad':
                    emociones = 'triste'
                if emociones == 'surprise':
                    emociones = 'sorprendido'
                if emociones == 'neutral':
                    emociones = 'neutral'

                # Race
                if race == 'asian':
                    race = 'asiatico'
                if race == 'indian':
                    race = 'indio'
                if race == 'black':
                    race = 'moreno'
                if race == 'white':
                    race = 'blanco'
                if race == 'latino hispanic':
                    race = 'latino'



            elif gen == 'Woman':
                gen = 'Mujer'

                # Emociones
                if emociones == 'angry':
                    emociones = 'enojada'
                if emociones == 'disgust':
                    emociones = 'disgustada'
                if emociones == 'fear':
                    emociones = 'miedosa'
                if emociones == 'happy':
                    emociones = 'feliz'
                if emociones == 'sad':
                    emociones = 'triste'
                if emociones == 'surprise':
                    emociones = 'sorprendida'
                if emociones == 'neutral':
                    emociones = 'neutral'

                # Race
                if race == 'asian':
                    race = 'asiatica'
                if race == 'black':
                    race = 'morena'
                if race == 'white':
                    race = 'blanca'
                if race == 'latino hispanic':
                    race = 'latina'

                # Mostramos info
            cv2.putText(frame, str(gen), (65, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.putText(frame, str(edad), (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.putText(frame, str(emociones), (75, 135), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.putText(frame, str(race), (75, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

            # Mostramos los fotogramas
        cv2.imshow(" Deteccion de Edad ", frame)

        # Leemos el teclado
        t = cv2.waitKey(5)
        if t == 27:
            break

cv2.destroyAllWindows()
cap.release()
