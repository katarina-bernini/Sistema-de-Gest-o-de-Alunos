# -*- coding: utf-8 -*-

def analisar_desempenho_alunos(dados_alunos):
    print("=" * 60)
    print("       RELATÓRIO DE ENGAJAMENTO        ")
    print("=" * 60)
    
    total_alunos = len(dados_alunos)
    soma_notas = 0
    soma_progresso = 0
    
    # Listas para categorizar os alunos
    alunos_destaque = []
    alunos_em_risco = []

    for aluno in dados_alunos:
        nome = aluno["nome"]
        nota = aluno["nota_final"]
        progresso = aluno["progresso_porcentagem"] # % de aulas assistidas
        
        # Acumulando para as médias gerais
        soma_notas += nota
        soma_progresso += progresso
        
        # Lógica de negócio para classificação
        if nota >= 8.5 and progresso >= 80:
            alunos_destaque.append(nome)
            status = " Destaque (Alto Engajamento)"
        elif nota < 6.0 or progresso < 40:
            alunos_em_risco.append(nome)
            status = " Alerta (Risco de Evasão)"
        else:
            status = " Regular"
            
        print(f"Aluno(a): {nome} | Nota: {nota} | Progresso: {progresso}% | Status: {status}")
    
    # Calculando estatísticas gerais da turma
    media_nota_turma = soma_notas / total_alunos if total_alunos > 0 else 0
    media_progresso_turma = soma_progresso / total_alunos if total_alunos > 0 else 0
    
    print("\n" + "=" * 60)
    print("                      MÉTRICAS GERAIS                      ")
    print("=" * 60)
    print(f"Total de Alunos Analisados: {total_alunos}")
    print(f"Média de Notas da Turma: {media_nota_turma:.2f}/10.0")
    print(f"Média de Progresso do Curso: {media_progresso_turma:.1f}%")
    
    print(f"\nAlunos Destaque para Feedback Positivo: {', '.join(alunos_destaque) if alunos_destaque else 'Nenhum'}")
    print(f"Alunos em Risco para Ação de Suporte: {', '.join(alunos_em_risco) if alunos_em_risco else 'Nenhum'}")
    print("=" * 60)

# Dados simulados (simulando uma resposta )
turma = [
    {"nome": "Ana Silva", "nota_final": 9.0, "progresso_porcentagem": 95},
    {"nome": "Carlos Souza", "nota_final": 5.5, "progresso_porcentagem": 30},
    {"nome": "Beatriz Santos", "nota_final": 7.5, "progresso_porcentagem": 65},
    {"nome": "Ricardo Lima", "nota_final": 4.0, "progresso_porcentagem": 50},
    {"nome": "Mariana Costa", "nota_final": 9.5, "progresso_porcentagem": 85}
]

# Executa a função passando os dados da turma
analisar_desempenho_alunos(turma)
