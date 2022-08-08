"""
63. Sistema de perguntas e respostas com dicionários em Python

Aqui vamos montar um sistema de perguntas e respostas utilizando dicionários.
"""

questions = {
    'q1' : {
        'question' : 'Quanto é 2 + 2?',
        'answer' : {
            'a' : '2',
            'b' : '4',
            'c' : '6'
        },
        'correct_answer' : 'b'
    },
    'q2' : {
        'question' : 'Quanto é 3 * 2?',
        'answer' : {
            'a' : '6',
            'b' : '8',
            'c' : '10'
        },
        'correct_answer' : 'a'
    },
    'q3' : {
        'question' : 'Quanto é 4 * 4?',
        'answer' : {
            'a' : '40',
            'b' : '16',
            'c' : '12'
        },
        'correct_answer' : 'b'
    },
    'q4' : {
        'question' : 'Quanto é 1024 / 4?',
        'answer' : {
            'a' : '250',
            'b' : '350',
            'c' : '256'
        },
        'correct_answer' : 'c'
    },
    'q5' : {
        'question' : 'Quanto é 7 * 8?',
        'answer' : {
            'a' : '66',
            'b' : '56',
            'c' : '76'
        },
        'correct_answer' : 'b'
    },
}

qtd_questions = len(questions)
hits = 0

print('Responda as perguntas')
print()

for pk, qv in questions.items():
    print(f"Pergunta: {qv['question']}")

    for op, answer in qv['answer'].items():
        print(f'[{op}] {answer}')

    answered = input('Resposta: ') 

    if answered == qv['correct_answer']:
        print('Aeeee!! Você acertou!!!')
        hits += 1
    else:
        print('Vixiii, você errou!')

    print()

qtd_hits = hits / qtd_questions * 100

print(f'Você acertou {hits} perguntas e a sua porcentagem foi de {qtd_hits}%.')
print()