import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        file = open("v_input.txt", 'a')
        file.write(text)
        file.write("\n")
        file.close()
    except:
        print("Sorry could not recognize what you said")
