import justpy as jp


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header, classes="bg-purple-700")

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode='left', bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        a_class = "p-2 m-2 text-lg text-purple-400 hover:text-purple-700"
        jp.A(a=qlist, text="Home", href="/", classes=a_class)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_class)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_class)
        jp.Br(a=qlist)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
                click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='Instant Dictionary')

        container = jp.QPageContainer(a=layout)
        con = jp.Div(a=container, classes="bg-purple-300 m-24 p-10 rounded")
        jp.Div(a=con, text="This is the home page", classes="text-4xl m-2")
        jp.Div(a=con, text="""
        This website was created by Martin Slater, 18th February 2021
        using JustPy and Tailwind CSS
        """, classes="text-lg")
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
