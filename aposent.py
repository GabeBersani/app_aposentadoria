import flet as ft
from flet.core import page
from flet.core.app_bar import AppBar
from flet import AppBar, ElevatedButton, Page, Text, View
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
    def gerar_rotas(e, txt_alerta=None):
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
                    "/simular_aposentadoria", [
                        AppBar(title=Text("simulação de aposentadoria"), center_title=True, bgcolor=Colors.PINK),

                        meu_genero,
                        idade,
                        tempo_contribuicao,
                        media_salarial,
                        opcao,
                        ElevatedButton(text="Calcular", on_click=verificar_campos),
                        ElevatedButton(text="regras", on_click=verificar_campos),
                        txt_alerta,

                    ]
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