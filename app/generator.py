def gerar_plano(plano):
    return {
        "escola": plano.get("escola", "Escola Exemplo"),
        "disciplina": plano.get("disciplina", "Matemática"),
        "objetivos": plano.get("objetivos", "Ensinar operações básicas."),
        "metodologia": plano.get("metodologia", "Uso de atividades interativas."),
        "recursos": plano.get("recursos", "Quadro, giz e livros."),
        "atividades": plano.get("atividades", "Resolução de problemas em grupo."),
        "avaliacao": plano.get("avaliacao", "Prova ao final da semana."),
        "competencias": ["Competência BNCC 1", "Competência BNCC 2"]
    }
