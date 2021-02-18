import justpy as jp


@jp.SetRoute("/")
def home():
    wp = jp.QuasarPage(tailwind=True)

    page = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    # jp.Div(a=page, classes="bg-gray-300")
    con = jp.Div(a=page, classes="bg-purple-300 m-24 p-10 rounded")

    line = jp.Div(a=con, classes="grid grid-cols-3 gap-4")
    in_1 = jp.Input(a=line, placeholder="Enter the first value", classes="form-input")
    in_2 = jp.Input(a=line, placeholder="Enter the second value", classes="form-input")
    result = jp.Div(a=line, text="Result goes here....")
    jp.QBtn(a=con, label="Calculate", color='purple', icon="calculator", click=sum_up, in1=in_1, in2 = in_2, total = result,
              classes="bg-purple-600 m-2 py-1 px-4 text-gray-800 rounded hover:bg-purple-800")
    jp.Div(a=con, text="interactive div", mouseenter=mouse_enter, mouseleave = mouse_leave)

    return wp


def sum_up(widget, msg):
    total = float(widget.in1.value) + float(widget.in2.value)
    widget.total.text = total
    print(total)

def mouse_enter(widget, msg):
    widget.text = "The mouse is in the house"

def mouse_leave(widget, msg):
    widget.text = "The mouse left"


jp.justpy()
