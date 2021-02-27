# Generated by Django 2.2.3 on 2019-12-02 09:34

from django.db import migrations

"""
    Mudança nas inscrições dos editais do PSCT 2020.1 devido ao cadastro incorreto de cursos 
    durante a configuração do sistema, conforme solicitado por Simão Viana da COMPEC, no dia 02 de 
    dezembro de 2018, por Simão Viana.

    Modificações:
    Candidatos inscritos no curso Técnico Integrado em Informática (INTEGRAL) - Campus Esperança
    * Migrados para o curso Técnico Integrado em Informática (DIURNO) - Campus Esperança

    Candidatos inscritos no curso Técnico Integrado em Mecânica (MATUTINO) - Campus João Pessoa
    * Migrados para o curso Técnico Integrado em Mecânica (VESPERTINO) - Campus João Pessoa
    
    Candidatos inscritos no curso Técnico Subsequente em Transporte Aquaviário (NOTURNO) - Campus 
    Cabedelo Centro
    * Migrados para o curso Técnico Subsequente em Transporte Aquaviário (NOTURNO) - Campus 
    Cabedelo Centro
    
    Candidatos inscritos no curso Técnico Subsequente em Instrumento Musical (VESPERTINO) - Campus 
    João Pessoa
    * Migrados para o curso Técnico Subsequente em Instrumento Musical (NOTURNO) - Campus João 
    Pessoa

"""


def change_inscricoes(apps, schema_editor):
    CursoNoCampus = apps.get_model("cursos.CursoNoCampus")
    Edital = apps.get_model("editais.edital")
    Inscricao = apps.get_model("psct.Inscricao")
    InscricaoPreAnalise = apps.get_model("psct.InscricaoPreAnalise")

    edital_147 = Edital.objects.filter(pk=120).last()
    informatica_diurno = CursoNoCampus.objects.filter(pk=74).last()
    informatica_integral = CursoNoCampus.objects.filter(pk=230).last()
    informatica_edital_147 = Inscricao.objects.filter(
        curso=informatica_integral, edital=edital_147
    )

    for i in informatica_edital_147:
        i.curso = informatica_diurno
        i.save()

        InscricaoPreAnalise.objects.filter(
            fase__edital=edital_147, candidato=i.candidato
        ).update(curso=informatica_diurno)

    mecanica_matutino = CursoNoCampus.objects.filter(pk=187).last()
    mecanica_verpertino = CursoNoCampus.objects.filter(pk=163).last()
    mecanica_edital_147 = Inscricao.objects.filter(
        curso=mecanica_matutino, edital=edital_147
    )

    for i in mecanica_edital_147:
        i.curso = mecanica_verpertino
        i.save()

        InscricaoPreAnalise.objects.filter(
            fase__edital=edital_147, candidato=i.candidato
        ).update(curso=mecanica_verpertino)

    edital_148 = Edital.objects.filter(pk=121).last()
    taquaviario_verpertino = CursoNoCampus.objects.filter(pk=229).last()
    taquaviario_noturno = CursoNoCampus.objects.filter(pk=3).last()
    inscricoes_edital_148 = Inscricao.objects.filter(
        curso=taquaviario_noturno, edital=edital_148
    )

    for i in inscricoes_edital_148:
        i.curso = taquaviario_verpertino
        i.save()

        InscricaoPreAnalise.objects.filter(
            fase__edital=edital_148, candidato=i.candidato
        ).update(curso=taquaviario_verpertino)

    edital_149 = Edital.objects.filter(pk=122).last()
    musica_verpertino = CursoNoCampus.objects.filter(pk=112).last()
    musica_noturno = CursoNoCampus.objects.filter(pk=228).last()
    inscricoes_edital_149 = Inscricao.objects.filter(
        curso=musica_verpertino, edital=edital_149
    )

    for i in inscricoes_edital_149:
        i.curso = musica_noturno
        i.save()

        InscricaoPreAnalise.objects.filter(
            fase__edital=edital_149, candidato=i.candidato
        ).update(curso=musica_noturno)


class Migration(migrations.Migration):

    dependencies = [
        ("psct", "0020_auto_20190709_1621"),
    ]

    operations = [migrations.RunPython(change_inscricoes, None)]