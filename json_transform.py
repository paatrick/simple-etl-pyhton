import pandas as pd

# colaboradores
colaboradores_df = pd.read_json(
    './data/json/dados_normalizados/colaboradores.json')


# generos
generos_df = pd.read_json(
    './data/json/dados_normalizados/generos.json')

colaboradores_df = colaboradores_df.merge(
    generos_df[['id_genero', 'nome_genero']], left_on='fk_genero', right_on='id_genero').drop(columns=['id_genero', 'fk_genero'])


# escolaridade
escolaridades_df = pd.read_json(
    './data/json/dados_normalizados/escolaridades.json')

colaboradores_df = colaboradores_df.merge(
    escolaridades_df[['id_escolaridade', 'nome_escolaridade']], left_on='fk_escolaridade', right_on='id_escolaridade').drop(columns=['id_escolaridade', 'fk_escolaridade'])


# contratos
contratos_df = pd.read_json(
    './data/json/dados_normalizados/contratos.json')

colaboradores_df = colaboradores_df.merge(
    contratos_df[['id_contrato', 'nome_contrato']], left_on='fk_contrato', right_on='id_contrato').drop(columns=['id_contrato', 'fk_contrato'])


# nacionalidades
nacionalidades_df = pd.read_json(
    './data/json/dados_normalizados/nacionalidades.json')

colaboradores_df = colaboradores_df.merge(
    nacionalidades_df[['id_nacionalidade', 'nome_nacionalidade']], left_on='fk_nacionalidade', right_on='id_nacionalidade').drop(columns=['id_nacionalidade', 'fk_nacionalidade'])


# data de admissão
datas_df = pd.read_json(
    './data/json/dados_normalizados/datas.json')

colaboradores_df = colaboradores_df.merge(
    datas_df[['id_data', 'data']].rename(columns={"data": "data_admissao"}), left_on='fk_data_admissao', right_on='id_data').drop(columns=['id_data', 'fk_data_admissao'])


# export para json
colaboradores_df.to_json('./exports/colaboradores_json.json',
                         orient='records', force_ascii=False)
