import random

def formatar_topicos(lista):
    return "\n".join([f"- {item}" for item in lista])

def gerar_resposta(materia, modo, pergunta):
    pergunta_limpa = pergunta.strip()

    if not pergunta_limpa:
        return {
            "titulo": "Pergunta vazia",
            "conteudo": "Digite uma pergunta ou tema para o Study+ te ajudar."
        }

    materia = (materia or "Geral").strip()
    modo = (modo or "explicar_resposta").strip()

    if modo == "explicar":
        return resposta_explicar(materia, pergunta_limpa)

    elif modo == "explicar_resposta":
        return resposta_explicar_resposta(materia, pergunta_limpa)

    elif modo == "revisao":
        return resposta_revisao(materia, pergunta_limpa)

    elif modo == "quiz":
        return resposta_quiz(materia, pergunta_limpa)

    elif modo == "resumo":
        return resposta_resumo(materia, pergunta_limpa)

    return {
        "titulo": "Modo não reconhecido",
        "conteudo": "O modo selecionado não foi encontrado."
    }


def resposta_explicar(materia, pergunta):
    explicacao = (
        f"Você pediu uma explicação sobre **{pergunta}** na matéria **{materia}**.\n\n"
        f"## Explicação\n"
        f"O ideal é entender primeiro o conceito principal desse tema, depois observar exemplos, "
        f"aplicações e palavras-chave importantes. No Study+, esse modo serve para te ajudar a "
        f"compreender o conteúdo de forma mais clara, como se fosse uma revisão guiada.\n\n"
        f"## Como estudar esse tema\n"
        f"- Identifique o assunto principal da pergunta\n"
        f"- Procure os conceitos mais importantes\n"
        f"- Relacione com exemplos\n"
        f"- Faça um resumo com suas próprias palavras\n\n"
        f"## Dica do Study+\n"
        f"Depois de entender a explicação, use o modo **Explicar + Resposta** ou **Quiz** para treinar."
    )

    return {
        "titulo": f"Explicação • {materia}",
        "conteudo": explicacao
    }


def resposta_explicar_resposta(materia, pergunta):
    conteudo = (
        f"Você pediu o modo **Explicar + Resposta** para **{pergunta}** em **{materia}**.\n\n"
        f"## 1. Explicação\n"
        f"Nesse modo, a ideia é primeiro entender o raciocínio do conteúdo e só depois chegar na resposta final. "
        f"Isso ajuda a estudar de verdade, em vez de apenas copiar a resposta.\n\n"
        f"## 2. Como pensar nesse tipo de questão\n"
        f"- Leia com atenção o que está sendo pedido\n"
        f"- Separe palavras-chave da pergunta\n"
        f"- Relacione com a matéria escolhida\n"
        f"- Organize a resposta por etapas\n\n"
        f"## 3. Resposta final\n"
        f"**Resposta resumida sobre “{pergunta}”**: o tema deve ser respondido usando os conceitos centrais da matéria "
        f"**{materia}**, com linguagem clara, organizada e objetiva.\n\n"
        f"## 4. Dica de prova\n"
        f"Se for uma questão discursiva, comece definindo o assunto, depois explique a ideia principal e finalize com uma conclusão curta."
    )

    return {
        "titulo": f"Explicar + Resposta • {materia}",
        "conteudo": conteudo
    }


def resposta_revisao(materia, pergunta):
    topicos = [
        f"Definição de {pergunta}",
        f"Características principais de {pergunta}",
        f"Exemplos importantes sobre {pergunta}",
        f"Possíveis relações de {pergunta} com outros conteúdos",
        f"Questões que podem cair na prova sobre {pergunta}"
    ]

    conteudo = (
        f"Modo **Revisão para Prova** ativado para o tema **{pergunta}** em **{materia}**.\n\n"
        f"## Roteiro de revisão\n"
        f"{formatar_topicos(topicos)}\n\n"
        f"## Como revisar bem\n"
        f"1. Leia um resumo do tema\n"
        f"2. Destaque palavras-chave\n"
        f"3. Faça 3 perguntas sobre o conteúdo\n"
        f"4. Tente responder sem olhar\n"
        f"5. Corrija o que errou\n\n"
        f"## Mini revisão pronta\n"
        f"Para revisar **{pergunta}**, foque no conceito principal, nos exemplos, nas aplicações e nos pontos que diferenciam esse conteúdo de outros da matéria **{materia}**.\n\n"
        f"## Dica do Study+\n"
        f"Depois da revisão, use o modo **Quiz** para testar se você realmente aprendeu."
    )

    return {
        "titulo": f"Revisão para Prova • {materia}",
        "conteudo": conteudo
    }


def resposta_quiz(materia, pergunta):
    perguntas = [
        f"O que é {pergunta}?",
        f"Quais são as principais características de {pergunta}?",
        f"Como {pergunta} pode aparecer em uma prova de {materia}?",
        f"Qual é a importância de {pergunta} dentro de {materia}?",
        f"Cite um exemplo relacionado a {pergunta}."
    ]

    random.shuffle(perguntas)

    conteudo = (
        f"Modo **Quiz** ativado para **{pergunta}** em **{materia}**.\n\n"
        f"## Perguntas para treinar\n"
        f"1. {perguntas[0]}\n"
        f"2. {perguntas[1]}\n"
        f"3. {perguntas[2]}\n\n"
        f"## Como usar o quiz\n"
        f"- Tente responder sozinho primeiro\n"
        f"- Depois confira no seu material\n"
        f"- Marque o que você não souber\n"
        f"- Volte ao modo **Explicar** ou **Resumo** para revisar\n\n"
        f"## Dica do Study+\n"
        f"Se quiser um treino mais forte, responda no caderno sem consultar nada por 5 minutos."
    )

    return {
        "titulo": f"Quiz • {materia}",
        "conteudo": conteudo
    }


def resposta_resumo(materia, pergunta):
    conteudo = (
        f"Modo **Resumo** ativado para **{pergunta}** em **{materia}**.\n\n"
        f"## Resumo rápido\n"
        f"O tema **{pergunta}** deve ser entendido a partir do seu conceito central, dos seus exemplos mais importantes "
        f"e da forma como ele aparece dentro da matéria **{materia}**.\n\n"
        f"## Resumo em tópicos\n"
        f"- Conceito principal do tema\n"
        f"- Palavras-chave importantes\n"
        f"- Exemplo ou aplicação\n"
        f"- O que mais pode cair na prova\n\n"
        f"## Como transformar isso em estudo de verdade\n"
        f"1. Leia o resumo\n"
        f"2. Reescreva com suas palavras\n"
        f"3. Faça 2 perguntas sobre o tema\n"
        f"4. Use o modo Quiz para testar"
    )

    return {
        "titulo": f"Resumo • {materia}",
        "conteudo": conteudo
    }
