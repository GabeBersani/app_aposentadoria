import flet as ft
from flet import AppBar, ElevatedButton, Text, View, colors
from flet.core.colors import Colors
from flet.core.dropdown import Option
from flet.core.textfield import TextField


def main(page: ft.Page):
    # Configuração da pagina
    page.title = "Exemplos de rota"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funções
    def gerar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text(""), bgcolor="PINK"),

                    ElevatedButton(text="Simular aposentadoria", width=page.window.width,
                                   on_click=lambda _: page.go("/simular_aposentadoria")),
                    ElevatedButton(text="Regras aposentadoria", width=page.window.width,
                                   on_click=lambda _: page.go("/regras")),

                ],
            )
        )

        if page.route == "/simular_aposentadoria":
            page.views.append(
                View(
                    "/simular_aposentadoria",
                    [
                        AppBar(title=Text("Inicio"), bgcolor="PINK"),
                        Text(value=f'Bem vindo(a) '),
                        idade,
                        genero,
                        temp_contribuicao,
                        media_salario,
                        ElevatedButton(
                            text="Aposentadoria por Idade",
                            on_click=lambda _: page.go("/aposentadoria_idade"),
                            width=page.window.width
                        ),
                        ElevatedButton(
                            text="Aposentadoria por Tempo de Contribuição",
                            on_click=lambda _: page.go("/aposentadoria_contribuicao"),
                            width=page.window.width
                        ),
                    ],
                )
            )

        elif page.route == "/aposentadoria_idade":
            page.views.append(
                View(
                    "/aposentadoria_idade",
                    [
                        AppBar(title=Text("Inicio"), bgcolor="PINK"),
                    ],
                )
            )

        elif page.route == "/aposentadoria_contribuicao":
            page.views.append(
                View(
                    "/aposentadoria_contribuicao",
                    [
                        AppBar(title=Text("Inicio"), bgcolor="PINK"),
                    ],
                )
            )

        elif page.route == "/regras":
            page.views.append(
                View(
                    "/regras",
                    [
                        AppBar(title=Text("Inicio"), bgcolor="PINK"),
                        Text(value="As regras de aposentadoria por idade em 2025 são: "
                                   "\n"
                                   "\n"
                                   " Aposentadoria por Idade: \n"
                                   "Homens: 65 anos de idade e pelo menos 15 anos de contribuição. \n"
                                   "Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n "
                                   "\n"
                                   "Aposentadoria por Tempo de Contribuição: \n "
                                   "Homens: 35 anos de contribuição. \n"
                                   "Mulheres: 30 anos de contribuição. \n"
                                   "\n"
                                   "Valor Estimado do Benefício: O valor da aposentadoria será uma média de 60% "
                                   "da média salarial informada, acrescido de 2% por ano que exceder o tempo mínimo "
                                   "de contribuição.")
                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    text = Text(value="", size=24)
    idade = ft.TextField(label="Idade atual", hint_text="Digite sua idade atual")
    genero = ft.Dropdown(
        label="Genero",
        options=[Option(key="Masc", text="Masculino"), Option(key="Fem", text="Feminino")], width=page.window.width,
    )
    temp_contribuicao = ft.TextField(label="Tempo de Contribuição", hint_text="Digite seu tempo de contribuição")
    media_salario = ft.TextField(label="Tempo de Média Salarial", hint_text="Digite sua média salarial")
    page.on_route_change = gerar_rotas
    page.on_view_pop = voltar
    page.go(page.route)


    def aposentadoria_idade(e):
        try:
            if genero.value == "Feminino":
                if int(idade.value) >= 62:
                    tmp = int(temp_contribuicao.value)
                    if tmp >= 15:
                        salario = media_salario.value
                        salario_60 = salario * 0.6
                        delta_tmp = (tmp - 15)
                        if delta_tmp > 0:
                            porcentagem = delta_tmp * 2
                            salario_60 = (salario_60 / 100) * porcentagem
                        text.value = f'O valor da aposentadoria é {salario_60}'
                        page.update()



                else:
                    delta_idade = 62 - int(idade.value)
                    text.value = f"Infelizmente não esta apto, faltam cerca de {delta_idade} para aposentar"
                    page.update()

            elif genero.value == "Masculino":
                if int(idade.value) >= 65:
                    tmp = int(temp_contribuicao.value)
                    if tmp >= 15:
                        salario = media_salario.value
                        salario_60 = salario * 0.6
                        delta_tmp = (tmp - 15)
                        if delta_tmp > 0:
                            porcentagem = delta_tmp * 2
                            salario_60 = (salario_60 / 100) * porcentagem
                        text.value = f'O valor da aposentadoria é {salario_60}'
                        page.update()

        except ValueError:
            text.value = 'Erro de valor'

ft.app(main)
