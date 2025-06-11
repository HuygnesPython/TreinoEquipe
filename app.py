#_______________________________
#Início                        |
import mysql.connector as my#  |
from pydantic import BaseModel#|
from fastapi import FastAPI#   |
def conectar_banco():#         |
    conexao = my.conexao(#     |
        host='localhost', #    |
        user='root', #         |
        password='',#          |
        db='eventos_db'#       |
    )#                         |
    return conexao#            |
app = FastAPI()#               |
#------------------------------|

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




# Deletar shows




# Atualizar shows




# Ver um show

