import justpy as jp
import definition
from webapp import layout
from webapp import page


class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        # Build the web page
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        con = jp.Div(a=container, classes="bg-purple-300 p-10 rounded")
        # two lines of titles
        jp.Div(a=con, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=con, text="Get the definition of any word instantly as you type", classes="text-lg")
        # line div creates a holder to put input box in so it can be declared after output div
        line = jp.Div(a=con, classes="grid grid-cols-2")
        # box where output is displayed listed before input box so input box can reference it
        output_div = jp.Div(a=con, classes="m-2 p-2 text-lg border-2 h-40")
        # box where input is typed
        input_box = jp.Input(a=line, placeholder="Type in a word here...", outputdiv=output_div,
                             classes="m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 "
                                     "focus:outline-none focus:border-purple-500 focus:bg-white")
        # dynamic method which calls get_definition as text is typed
        input_box.on('input', cls.get_definition)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        """
        gets the definition of a word using definition.Definition
        :param: widget is the widget which calls the function
        :return: none
        """
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)
