from openai import OpenAI
import os
import requests
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Creación de roles
conversation = [
    {"role": "system", "content": "Eres un asistente especializado en marketing que crea textos publicitarios breves, atractivos y persuasivos para promocionar eventos musicales en redes sociales."},
    {"role": "user", "content": "Crea un texto publicitario breve y atractivo para promocionar el evento [Nativo], cuya temática es [Fiesta en la playa con el atardecer]. El mensaje debe captar la atención en menos de 50 palabras, con un tono juvenil, entusiasta y playa e incluir un llamado a la acción. No incluir hashtags pero sí incluye emojis, pero no abuses"}
]

#Llamado al modelo
respuesta = client.chat.completions.create(
    model="gpt-4o-mini", 
    messages=conversation,
    max_tokens=200,
    temperature=0.5,
)

# Mostrar la respuesta
message = respuesta.choices[0].message

print("Texto para publicidad:\n", message.content)


# MODELO TEXTO A IMAGEN

prompt_imagen = ("Imagen realista de una fiesta en la playa al atardecer. Muestra a un grupo de personas jóvenes bailando y disfrutando frente al mar, con sonrisas y expresiones alegres. Los rostros deben ser claros, bien definidos y con proporciones naturales, estilo fotográfico profesional. Incluye un DJ en una cabina iluminada al fondo, palmeras y luces festivas colgantes. Colores cálidos como naranja, rosa y azul, transmitiendo energía y alegría. Formato cuadrado y estilo publicitario para redes sociales ") 

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt_imagen,
    size="1024x1024"
)

image_url = response.data[0].url
print(f"Imagen generada: {image_url}")


img_data = requests.get(image_url).content
with open('arte_nativo.png', 'wb') as handler:
    handler.write(img_data)

print("Fin: Imagen generada")