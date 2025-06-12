#////////////Início////////////
#______________________________
import mysql.connector as my#   |
from pydantic import BaseModel# |
from fastapi import FastAPI#    |
class NovoShow(BaseModel):#     |
    nome:str#                   |
    data_show:str#              |
    descricao:str#              |
class DeletarShow(BaseModel):#  |
    id:int#                     |
class AtualizarShow(BaseModel):#|
    nome:str#                   |
    data_show:str#              |
    descricao:str#              |
def conectar_banco():#          |
    conexao = my.connect(#      |
        host='localhost', #     |
        user='root', #          |
        password='',#           |
        db='eventos_db'#        |
    )#                          |
    return conexao#             |
app = FastAPI()#                |
#-------------------------------
# Ver shows
@app.get('/VerShows')
def ver_shows():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = 'select * from show_db'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado
# Criar shows
@app.post('/CriarShows')
def criar_show(show:NovoShow):
    # print(show.nome, show.data_show, show.descricao)
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = f'insert into show_db(nome,data_show,descricao) values ("{show.nome}","{show.data_show}","{show.descricao}")'
    cursor.execute(sql)
    conexao.commit()
    conexao.close()
    return {'Criado!'}
# Deletar shows
@app.delete('/DeletarShow')
def deletar_show(show:DeletarShow):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = f'delete from show_db where id = "{show.id}"'
    cursor.execute(sql)
    conexao.commit()
    conexao.close()
    return {'Deletado!'}
# Atualizar shows
@app.put('/AtualizarShow/{id}')
def atualizar_show(show:AtualizarShow):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = f'update show_db set nome = "{show.nome}", data_show = "{show.data_show}", descricao = "{show.descricao}"'
    cursor.execute(sql)
    conexao.commit()
    conexao.close()
    return {'Deletado!'}
# Ver um show
@app.get('/VerShow/{id}')
def ver_show_id(id:int):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = f'select * from show_db where id = "{id}"'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado