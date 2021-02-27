# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-08 10:39
from __future__ import unicode_literals

import base.history
import cursos.models
import cursos.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("processoseletivo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AtoRegulatorio",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "arquivo",
                    models.FileField(
                        help_text="Apenas arquivos .pdf no tamanho máximo de 2MB.",
                        max_length=255,
                        upload_to=cursos.models.generate_atoregulatorio_curso_path,
                        validators=[
                            cursos.validators.validate_file_size,
                            cursos.validators.validate_file_type,
                        ],
                    ),
                ),
                (
                    "descricao",
                    models.CharField(max_length=255, verbose_name="Descrição"),
                ),
                ("numero", models.IntegerField(verbose_name="Número")),
                ("ano", models.IntegerField()),
            ],
            options={
                "verbose_name": "Ato Regulatorio",
                "verbose_name_plural": "Atos Regulatorios",
            },
        ),
        migrations.CreateModel(
            name="Campus",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(max_length=55, unique=True, verbose_name="Nome"),
                ),
                (
                    "sigla",
                    models.CharField(max_length=5, unique=True, verbose_name="Sigla"),
                ),
                ("endereco", models.CharField(max_length=255, verbose_name="Endereço")),
                ("telefone", models.CharField(max_length=15)),
                (
                    "mapa",
                    models.CharField(
                        blank=True,
                        help_text='Endereço da opção "Incorporar Mapa" do Google Maps. Veja este tutorial de como fazer: https://support.google.com/maps/answer/3544418?hl=pt-BR',
                        max_length=1025,
                        null=True,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Campi",},
        ),
        migrations.CreateModel(
            name="Cidade",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                (
                    "uf",
                    models.CharField(
                        choices=[
                            ("AC", "Acre"),
                            ("AL", "Alagoas"),
                            ("AP", "Amapa"),
                            ("AM", "Amazonas"),
                            ("BA", "Bahia"),
                            ("CE", "Ceará"),
                            ("DF", "Distrito Federal"),
                            ("ES", "Espírito Santo"),
                            ("GO", "Goiás"),
                            ("MA", "Maranhão"),
                            ("MT", "Mato Grosso"),
                            ("MS", "Mato Grosso do Sul"),
                            ("MG", "Minas Gerais"),
                            ("PA", "Pará"),
                            ("PB", "Paraíba"),
                            ("PR", "Paraná"),
                            ("PE", "Pernambuco"),
                            ("PI", "Piauí"),
                            ("RJ", "Rio de Janeiro"),
                            ("RN", "Rio Grande do Norte"),
                            ("RS", "Rio Grande do Sul"),
                            ("RO", "Rondônia"),
                            ("RR", "Roraima"),
                            ("SC", "Santa Catarina"),
                            ("SP", "São Paulo"),
                            ("SE", "Sergipe"),
                            ("TO", "Tocantis"),
                        ],
                        max_length=2,
                        verbose_name="UF",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Coordenador",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "telefone",
                    models.CharField(
                        help_text="Informar o telefone institucional.",
                        max_length=15,
                        verbose_name="Telefone",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Informar o e-mail institucional.",
                        max_length=128,
                        verbose_name="E-mail",
                    ),
                ),
            ],
            options={
                "verbose_name": "Coordenador",
                "verbose_name_plural": "Coordenadores",
            },
        ),
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(max_length=255, unique=True, verbose_name="Nome"),
                ),
                ("perfil_unificado", models.TextField(verbose_name="Perfil Unificado")),
            ],
            options={
                "ordering": ("nome",),
                "verbose_name": "Curso",
                "verbose_name_plural": "Cursos",
            },
        ),
        migrations.CreateModel(
            name="CursoNoCampus",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "turno",
                    models.CharField(
                        choices=[
                            ("MATUTINO", "Matutino"),
                            ("VESPERTINO", "Vespertino"),
                            ("NOTURNO", "Noturno"),
                            ("INTEGRAL", "Integral"),
                            ("DIURNO", "Diurno"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "formacao",
                    models.CharField(
                        choices=[
                            ("INTEGRADO", "Técnico Integrado"),
                            ("SUBSEQUENTE", "Técnico Subsequente"),
                            ("TECNOLOGICO", "Tecnológico"),
                            ("BACHARELADO", "Bacharelado"),
                            ("LICENCIATURA", "Licenciatura"),
                            ("ESPECIALIZACAO", "Especialização"),
                            ("MESTRADO", "Mestrado"),
                            ("DOUTORADO", "Doutorado"),
                        ],
                        max_length=16,
                        verbose_name="Formação",
                    ),
                ),
                (
                    "modalidade",
                    models.CharField(
                        choices=[("PRESENCIAL", "Presencial"), ("EAD", "A distância")],
                        max_length=16,
                    ),
                ),
                (
                    "codigo",
                    models.IntegerField(
                        help_text="Codigo do curso cadastrado no e-MEC",
                        unique=True,
                        verbose_name="Codigo do Curso (e-Mec)",
                    ),
                ),
                (
                    "inicio",
                    models.DateField(
                        blank=True,
                        help_text="Data de inicio do funcionamento do curso",
                        verbose_name="Inicio",
                    ),
                ),
                (
                    "termino",
                    models.DateField(
                        blank=True,
                        help_text="Data de encerramento do curso",
                        null=True,
                        verbose_name="Termino",
                    ),
                ),
                (
                    "conceito",
                    models.CharField(
                        blank=True,
                        default=0,
                        help_text="Conceito do Curso",
                        max_length=50,
                        verbose_name="Conceito",
                    ),
                ),
                (
                    "cpc",
                    models.CharField(
                        blank=True,
                        default=0,
                        help_text="Conceito Preliminar de Curso",
                        max_length=2,
                        verbose_name="CPC",
                    ),
                ),
                (
                    "enade",
                    models.CharField(
                        blank=True,
                        default=0,
                        help_text="Nota do Curso no ENADE",
                        max_length=1,
                        verbose_name="ENADE",
                    ),
                ),
                (
                    "ch_minima",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="Carga horária mínima para a integralização do curso",
                        verbose_name="Carga Horária Mínima",
                    ),
                ),
                (
                    "ch_total",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="Carga horária total do curso",
                        verbose_name="Carga Horária Total",
                    ),
                ),
                (
                    "ch_estagio",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="Carga horária total de estágio necessária para a integralização do curso",
                        verbose_name="Carga Horária de Estágio",
                    ),
                ),
                (
                    "ch_tcc",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="Carga horária necessária para a execução do Trabalho de Conclusão de Curso",
                        verbose_name="Carga Horária de TCC",
                    ),
                ),
                (
                    "ch_rel_estagio",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="Carga horária necessária para a execução do relatório de estágio",
                        verbose_name="Carga Horária de Relatório de Estágio",
                    ),
                ),
                (
                    "ch_atividades_comp",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="Carga horária mínima de atividades complementares necessárias à integralização do curso",
                        verbose_name="Carga Horária de Atividades Complementares",
                    ),
                ),
                (
                    "periodo_min_int",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="Quantidade Mínima de bimestres/semestres/anos para a integralização do curso",
                        verbose_name="Período Mínimo para Integralização",
                    ),
                ),
                ("publicado", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Curso no Campus",
                "verbose_name_plural": "Cursos nos Campi",
            },
            bases=(models.Model, base.history.HistoryMixin),
        ),
        migrations.CreateModel(
            name="Disciplina",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="DisciplinaCurso",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("periodo", models.IntegerField(default=1, verbose_name="Período")),
                ("ch", models.IntegerField(default=0, verbose_name="Carga Horária")),
            ],
            options={
                "verbose_name": "Disciplina do Curso",
                "verbose_name_plural": "Disciplinas dos Cursos",
            },
        ),
        migrations.CreateModel(
            name="Docente",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255, verbose_name="Nome")),
                (
                    "matricula",
                    models.CharField(
                        help_text="Sem dígito verificador.",
                        max_length=8,
                        unique=True,
                        verbose_name="Matrícula",
                    ),
                ),
                (
                    "titulacao",
                    models.CharField(
                        choices=[
                            ("GRADUACAO", "Graduação"),
                            ("APERFEICOAMENTO", "Aperfeiçoamento"),
                            ("ESPECIALIZACAO", "Especialização"),
                            ("MESTRADO", "Mestrado"),
                            ("DOUTORADO", "Doutorado"),
                        ],
                        max_length=15,
                        verbose_name="Titulação",
                    ),
                ),
                (
                    "admissao",
                    models.DateField(
                        help_text="Data que entrou em exercício como docente da instituição.",
                        verbose_name="Admissão",
                    ),
                ),
                (
                    "lattes",
                    models.URLField(
                        help_text="Endereço para o currículo Lattes.",
                        max_length=100,
                        unique=True,
                        verbose_name="Lattes",
                    ),
                ),
                (
                    "rt",
                    models.CharField(
                        choices=[
                            ("DE", "Dedicação Exclusiva"),
                            ("TI", "Tempo Integral (40h)"),
                            ("TP", "Tempo Parcial (20h)"),
                        ],
                        max_length=10,
                        verbose_name="Regime de Trabalho",
                    ),
                ),
            ],
            options={"verbose_name": "Docente", "verbose_name_plural": "Docentes",},
        ),
        migrations.CreateModel(
            name="Documento",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "descricao",
                    models.CharField(max_length=255, verbose_name="Descrição"),
                ),
                (
                    "arquivo",
                    models.FileField(
                        help_text="Apenas arquivos .pdf no tamanho máximo de 2MB.",
                        upload_to=cursos.models.generate_documento_curso_path,
                        verbose_name="Arquivo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Historico",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("atributo_alterado", models.CharField(max_length=20)),
                ("valor_antigo", models.TextField()),
                ("valor_novo", models.TextField()),
                ("data_alteracao", models.DateField(auto_now=True)),
                (
                    "curso_alterado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cursos.Curso"
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name": "Historico", "verbose_name_plural": "Historico",},
        ),
        migrations.CreateModel(
            name="IES",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo", models.IntegerField(unique=True, verbose_name="Código")),
                (
                    "uf",
                    models.CharField(
                        choices=[
                            ("AC", "Acre"),
                            ("AL", "Alagoas"),
                            ("AP", "Amapa"),
                            ("AM", "Amazonas"),
                            ("BA", "Bahia"),
                            ("CE", "Ceará"),
                            ("DF", "Distrito Federal"),
                            ("ES", "Espírito Santo"),
                            ("GO", "Goiás"),
                            ("MA", "Maranhão"),
                            ("MT", "Mato Grosso"),
                            ("MS", "Mato Grosso do Sul"),
                            ("MG", "Minas Gerais"),
                            ("PA", "Pará"),
                            ("PB", "Paraíba"),
                            ("PR", "Paraná"),
                            ("PE", "Pernambuco"),
                            ("PI", "Piauí"),
                            ("RJ", "Rio de Janeiro"),
                            ("RN", "Rio Grande do Norte"),
                            ("RS", "Rio Grande do Sul"),
                            ("RO", "Rondônia"),
                            ("RR", "Roraima"),
                            ("SC", "Santa Catarina"),
                            ("SP", "São Paulo"),
                            ("SE", "Sergipe"),
                            ("TO", "Tocantis"),
                        ],
                        max_length=2,
                        verbose_name="UF",
                    ),
                ),
                (
                    "nome",
                    models.CharField(max_length=255, unique=True, verbose_name="Nome"),
                ),
                (
                    "sigla",
                    models.CharField(max_length=10, unique=True, verbose_name="Sigla"),
                ),
                (
                    "ci",
                    models.CharField(
                        max_length=10, verbose_name="Conceito Institucional"
                    ),
                ),
            ],
            options={
                "verbose_name": "Instituição de Ensino",
                "verbose_name_plural": "Instituições de Ensino",
            },
        ),
        migrations.CreateModel(
            name="PalavraChave",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "palavra_chave",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Palavras-chave"
                    ),
                ),
            ],
            options={
                "verbose_name": "Palavra-chave",
                "verbose_name_plural": "palavras-chave",
            },
        ),
        migrations.CreateModel(
            name="Polo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "horario_funcionamento",
                    models.CharField(
                        max_length=100, verbose_name="Horário de Funcionamento"
                    ),
                ),
                ("endereco", models.CharField(max_length=255, verbose_name="Endereço")),
                ("telefone", models.CharField(max_length=15)),
                (
                    "mapa",
                    models.CharField(
                        blank=True,
                        help_text='Endereço da opção "Incorporar Mapa" do Google Maps. Veja este tutorial de como fazer: https://support.google.com/maps/answer/3544418?hl=pt-BR',
                        max_length=1025,
                        null=True,
                    ),
                ),
                (
                    "cidade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cursos.Cidade"
                    ),
                ),
            ],
            options={
                "ordering": ["cidade__nome"],
                "verbose_name": "Polo",
                "verbose_name_plural": "Polos",
            },
        ),
        migrations.CreateModel(
            name="TipoAtoRegulatorio",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=128, unique=True)),
            ],
            options={
                "verbose_name": "Tipo de Ato Regulatório",
                "verbose_name_plural": "Tipos de Atos Regulatórios",
            },
        ),
        migrations.CreateModel(
            name="TipoDocumento",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=128, unique=True)),
                (
                    "obrigatorio",
                    models.BooleanField(
                        default=False,
                        help_text="Ao marcar este campo, você exige que o coordenador do curso cadastre pelo menos um documento deste tipo.",
                        verbose_name="Obrigatório",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tipo de Documento",
                "verbose_name_plural": "Tipos de Documentos",
            },
        ),
        migrations.CreateModel(
            name="VagasEAD",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vagas_s1", models.IntegerField(verbose_name="Vagas no 1º Semestre")),
                ("vagas_s2", models.IntegerField(verbose_name="Vagas no 2º Semestre")),
                (
                    "polo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cursos.Polo"
                    ),
                ),
            ],
            options={
                "verbose_name": "Vaga em um Polo EAD",
                "verbose_name_plural": "Vagas por Polo EAD",
            },
        ),
        migrations.CreateModel(
            name="CursoEAD",
            fields=[
                (
                    "cursonocampus_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="cursos.CursoNoCampus",
                    ),
                ),
            ],
            options={"verbose_name": "Curso EAD", "verbose_name_plural": "Cursos EAD",},
            bases=("cursos.cursonocampus",),
        ),
        migrations.CreateModel(
            name="CursoPresencial",
            fields=[
                (
                    "cursonocampus_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="cursos.CursoNoCampus",
                    ),
                ),
                (
                    "vagas_s1",
                    models.IntegerField(
                        blank=True, verbose_name="Vagas no 1º Semestre"
                    ),
                ),
                (
                    "vagas_s2",
                    models.IntegerField(
                        blank=True, verbose_name="Vagas no 2º Semestre"
                    ),
                ),
            ],
            options={
                "verbose_name": "Curso Presencial",
                "verbose_name_plural": "Cursos Presenciais",
            },
            bases=("cursos.cursonocampus",),
        ),
        migrations.AddField(
            model_name="documento",
            name="curso",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cursos.CursoNoCampus"
            ),
        ),
        migrations.AddField(
            model_name="documento",
            name="tipo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cursos.TipoDocumento"
            ),
        ),
        migrations.AddField(
            model_name="disciplinacurso",
            name="curso",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cursos.CursoNoCampus"
            ),
        ),
        migrations.AddField(
            model_name="disciplinacurso",
            name="disciplina",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cursos.Disciplina"
            ),
        ),
        migrations.AddField(
            model_name="disciplinacurso",
            name="docentes",
            field=models.ManyToManyField(to="cursos.Docente"),
        ),
        migrations.AddField(
            model_name="cursonocampus",
            name="campus",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cursos.Campus"
            ),
        ),
        migrations.AddField(
            model_name="cursonocampus",
            name="curso",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cursos.Curso"
            ),
        ),
        migrations.AddField(
            model_name="cursonocampus",
            name="forma_acesso",
            field=models.ManyToManyField(
                blank=True, to="processoseletivo.ProcessoSeletivo"
            ),
        ),
        migrations.AddField(
            model_name="cursonocampus",
            name="palavras_chave",
            field=models.ManyToManyField(blank=True, to="cursos.PalavraChave"),
        ),
        migrations.AddField(
            model_name="curso",
            name="campus",
            field=models.ManyToManyField(
                through="cursos.CursoNoCampus", to="cursos.Campus"
            ),
        ),
        migrations.AddField(
            model_name="coordenador",
            name="curso",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="cursos.CursoNoCampus"
            ),
        ),
        migrations.AddField(
            model_name="coordenador",
            name="docente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cursos.Docente"
            ),
        ),
        migrations.AddField(
            model_name="campus",
            name="cidade",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cursos.Cidade"
            ),
        ),
        migrations.AddField(
            model_name="campus",
            name="diretor_ensino",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="cursos.Docente",
                verbose_name="Diretor de Ensino",
            ),
        ),
        migrations.AddField(
            model_name="campus",
            name="ies",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="campi",
                to="cursos.IES",
                verbose_name="Instituição de Ensino",
            ),
        ),
        migrations.AddField(
            model_name="atoregulatorio",
            name="curso",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cursos.CursoNoCampus"
            ),
        ),
        migrations.AddField(
            model_name="atoregulatorio",
            name="tipo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="cursos.TipoAtoRegulatorio",
            ),
        ),
        migrations.AddField(
            model_name="vagasead",
            name="curso",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cursos.CursoEAD"
            ),
        ),
    ]