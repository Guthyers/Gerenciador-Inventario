import json
from rich import print


with open('inventario.json', 'r') as inventariojson: # as é o mesmo que definir apelido 
    arquivodedados = json.load(inventariojson)
#print(json.dumps(leitura, indent=4)) # O indent deixa o print bonito


class Gerenciamento:                                                                                  

    def __init__(self, dados): #dados está recebendo o conteudo do json
        self.dados = dados

    def listar(self):
        return self.dados

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

        with open ("inventario.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.dados, arquivo, indent=4, ensure_ascii=False)

        return "item adicionado com sucesso"

cliente = Gerenciamento(arquivodedados)
c1 = Gerenciamento(arquivodedados)

cliente.listar()
print(c1.consultar("caneta"))