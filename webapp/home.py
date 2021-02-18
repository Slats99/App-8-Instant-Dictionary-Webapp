import justpy as jp


class Home:
    path = "/"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        con = jp.Div(a=div, classes="bg-purple-300 m-24 p-10 rounded")
        jp.Div(a=con, text="This is the home page", classes="text-4xl m-2")
        jp.Div(a=con, text="""
        This website was created by Martin Slater, 18th February 2021
        using JustPy and Tailwind CSS
        """, classes="text-lg")
        return wp
