import justpy as jp

class DefaultLayout(jp.QLayout):

    def __init__(self, view="hHh lpR fFf", **kwargs):
        super().__init__(view=view, **kwargs)

        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header, classes="bg-purple-700")

        drawer = jp.QDrawer(a=self, show_if_above=True, v_mode='left', bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        a_class = "p-2 m-2 text-lg text-purple-400 hover:text-purple-700"
        jp.A(a=qlist, text="Home", href="/", classes=a_class)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_class)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_class)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Flat Mate Bill", href="/fmb", classes=a_class)
        jp.Br(a=qlist)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
                click=self.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='OOP course modules')

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
