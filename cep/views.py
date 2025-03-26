from django.shortcuts import render
import requests

def busca_cep(request):
    botao = False
    info = []

    if request.method == 'POST':
        cep = request.POST.get('cep')

        if not cep:
            info.append("CEP não informado.")
            botao = True
            return render(request, 'home.html', {'botao': botao, 'info': info})
        
        link = f"https://viacep.com.br/ws/{cep}/json/"

        try:
            requisicao = requests.get(link)
            dic = requisicao.json()
            
            if 'erro' in dic:
                info.append(f"CEP {cep} não encontrado.")
            else:
                info = [
                    f"<strong>📍 CEP:</strong> {dic.get('cep', 'N/A')}",
                    f"<strong>🏠 Rua:</strong> {dic.get('logradouro', 'N/A')}",
                    f"<strong>🧱 Complemento:</strong> {dic.get('complemento', 'N/A')}",
                    f"<strong>🏘️ Bairro:</strong> {dic.get('bairro', 'N/A')}",
                    f"<strong>🌇 Cidade 🇧🇷:</strong> {dic.get('localidade', 'N/A')}",
                    f"<strong>🚗 Estado 🇧🇷:</strong> {dic.get('estado', 'N/A')}",
                    f"<strong>📝 UF:</strong> {dic.get('uf', 'N/A')}",
                    f"<strong>📞 DDD:</strong> {dic.get('ddd', 'N/A')}"
                ]

            botao = True

        except requests.exceptions.RequestException:
            info.append("CEP inválido.")
            botao = True

        return render(request, 'home.html', {'botao': botao, 'info': info})
    else:
        return render(request, 'home.html')