import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

def transformar_audio_texto(): 
    # Almacenar el recognizer en una variable
    recognizer = sr.Recognizer()
    # Configurar micrófono
    with sr.Microphone() as origen:
        # Tiempo de espera
        recognizer.pause_threshold = 0.8
        # Informar que la grabación ha empezado
        print('Grabación en marcha ...')
        # Almacenar el audio en una variable
        audio = recognizer.listen(origen)
        try:
            # Buscar en google lo que haya escuchado
            consulta = recognizer.recognize_google_cloud(audio, language='es-es')
            # Prueba de que se ha podido transcribir el texto
            print(f'Consulta: {consulta}')
            return consulta
        except sr.UnknownValueError: 
            # Prueba de audio incomprendido
            print('Audio no entendido')
            return 'Sigo esperando'
        except sr.RequestError:
            # Prueba de audio incomprendido
            print('Sin servicio')
            return 'Sigo esperando'
        except:
            # Prueba de audio incomprendido
            print('Algo salió mal')
            return 'Sigo esperando'
        
transformar_audio_texto()
            
            
