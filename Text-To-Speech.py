from gtts import gTTS

text = "Si Dios es todopoderoso, por qué necesita un enemigo? Los dijeron que el diablo es el adversario, el rebelde, el que arruinó el plan perfecto. Pero piensa esto: si Dios es omnisciente, ya sabía que Lucifer se rebelaría. Si es omnipotente Podía impedirlo. Y si no lo impidió, entonces no fue accidente, fue diseño. El mal no sería un error, sería un mecanismo. Sin oscuridad no hay contraste. Sin tentación no hay elección. Sin caída no hay conciencia. Y si el diablo no es el enemigo de Dios, sino la herramienta que activa el libre albedrío, Lucifer significa portador de luz! La caída no destruyó el plan, lo puso en movimiento. Porque un universo sin oposición sería un universo estático. Y la conciencia solo despierta cuando algo la desafía. Tal vez. Dios no lucha contra el diablo, tal vez lo necesita, y eso cambia todo."
tts = gTTS(text=text, lang='es')

tts.save("C:\\Users\\jerie\\OneDrive\\Desktop\\tts\\speech.mp3")

print("Speech saved as speech.mp3")