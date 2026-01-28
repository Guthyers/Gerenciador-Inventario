import json
from rich import print # biblioteca c/ funções grafica emoji, tabelas e cores


with open('inventario.json', 'r') as inventariojson: # as é o mesmo que definir apelido # r para leitura 
    arquivodedados = json.load(inventariojson)



class Gerenciamento:                                                                                  

    def __init__(self, dados): # dados está recebendo o conteudo do json
        self.dados = dados

    def listar(self):
        return self.dados # me retorna toda a informação do dados

    def consultar(self, nome_procurado):
        for registro in self.dados:
            if registro.get("item") == nome_procurado:
                return registro
        return "Item não encontrado"

    def adicionar(self, item, estoque, descricao, ativo=True ):
        novo_id = max(registro["id"] for registro in self.dados) + 1

        novo_item ={
            "id": novo_id,
            "item": item,
            "estoque": estoque,
            "descricao": descricao,
            "ativo": ativo
        }

        self.dados.append(novo_item)

        with open ("inventario.json", "w", encoding="utf-8") as arquivo: # w para gravação
            json.dump(self.dados, arquivo, indent=4, ensure_ascii=False)

        return "item adicionado com sucesso"

cliente = Gerenciamento(arquivodedados) #cliente recebe a classe que instância arquivodedados, no caso o json   


#cliente.listar() #cliente chama a função listar 
print(cliente.listar()) #exibe a lista