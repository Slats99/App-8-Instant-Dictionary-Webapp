import justpy as jp
from webapp import layout
from webapp import page


class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        con = jp.Div(a=container, classes="bg-purple-300 m-24 p-10 rounded")
        jp.Div(a=con, text="This is the about page", classes="text-4xl m-2")
        jp.Div(a=con, text="""
        This website was created by Martin Slater, 18th February 2021
        using JustPy and Tailwind CSS
        """, classes="text-lg")
        return wp

