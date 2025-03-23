import requests
import tkinter as tk
from tkinter import messagebox

# Substitua pela sua chave de API do OpenWeatherMap
API_KEY = "032ed1b40ebb387269fa16f348125483"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def buscar_previsao():
    cidade = entrada_cidade.get()
    if not cidade:
        messagebox.showwarning("Aviso", "Por favor, digite uma cidade!")
        return
    
    params = {
        "q": cidade + ",BR",  # Especifica que queremos cidades do Brasil
        "appid": API_KEY,
        "lang": "pt",
        "units": "metric"  # Retorna temperatura em Celsius
    }
    
    resposta = requests.get(BASE_URL, params=params)
    dados = resposta.json()
    
    if resposta.status_code == 200:
        descricao = dados['weather'][0]['description'].capitalize()
        temperatura = dados['main']['temp']
        umidade = dados['main']['humidity']
        
        resultado = (f"Cidade: {cidade}\n"
                     f"Descrição: {descricao}\n"
                     f"Temperatura: {temperatura}°C\n"
                     f"Umidade: {umidade}%")
        label_resultado.config(text=resultado)
    else:
        messagebox.showerror("Erro", "Cidade não encontrada!")

# Criando a interface gráfica
root = tk.Tk()
root.title("Previsão do Tempo")
root.geometry("300x250")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Digite a cidade:").pack()
entrada_cidade = tk.Entry(frame)
entrada_cidade.pack(pady=5)

btn_buscar = tk.Button(frame, text="Buscar", command=buscar_previsao)
btn_buscar.pack()

label_resultado = tk.Label(root, text="", justify="left", font=("Arial", 10))
label_resultado.pack(pady=10)

root.mainloop()
