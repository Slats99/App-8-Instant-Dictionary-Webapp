import flat
import justpy as jp
from webapp import layout
from webapp import page


class FlatMateBill(page.Page):
    path = "/fmb"

    @classmethod
    def serve(cls, req):
        # Build the web page add layout and place this page in container
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        # classes for input boxes and labels
        input_class = "m-2 bg-gray-200 border-2 border-gray-200 rounded py-2 px-4 " \
                      "focus:outline-none focus:border-purple-500 focus:bg-white"
        label_class = "m-2 py-2 px-4"

        # create container box for the app
        con = jp.Div(a=container, classes="bg-purple-300 p-10 m-10 rounded")


        # two lines of titles
        jp.Div(a=con, text="Flatmates Bill", classes="text-4xl m-2")
        jp.Div(a=con, text="Get the amount of a bill two flatmates owe based on days in the house", classes="text-lg")

        # four lines for the input boxes and button
        l_fm1 = jp.Div(a=con, classes="grid grid-cols-4")
        l_fm2 = jp.Div(a=con, classes="grid grid-cols-4")
        l_bill = jp.Div(a=con, classes="grid grid-cols-4")
        # div for output
        output_div = jp.Div(a=con, classes="m-2 p-2 text-lg border-2 h-10")
        l_btn = jp.Div(a=con, classes="grid grid-cols-2")



        # boxes where input is typed
        jp.Div(a=l_fm1, text="1st Flatmate's name", classes=label_class)
        i_fm1_name = jp.Input(a=l_fm1, value="Martin", classes=input_class)
        jp.Div(a=l_fm1, text="days in the house", classes=label_class)
        i_fm1_days = jp.Input(a=l_fm1, value="28", classes=input_class)

        jp.Div(a=l_fm2, text="2nd Flatmate's name", classes=label_class)
        i_fm2_name = jp.Input(a=l_fm2, value="Will", classes=input_class)
        jp.Div(a=l_fm2, text="days in the house", classes=label_class)
        i_fm2_days = jp.Input(a=l_fm2, value="25", classes=input_class)

        jp.Div(a=l_bill, text="Bill amount", classes=label_class)
        i_bill_amt = jp.Input(a=l_bill, value="120", classes=input_class)
        jp.Div(a=l_bill, text="Bill period", classes=label_class)
        i_bill_period = jp.Input(a=l_bill, placeholder="e.g.: February 2021", classes=input_class)

        jp.Button(a=l_btn, text="calculate", click=cls.get_results, classes="bg-purple-700 rounded p-2 m-2",
                  fm1_name=i_fm1_name, fm2_name=i_fm2_name,
                  fm1_days=i_fm1_days, fm2_days=i_fm2_days,
                  bill_amt=i_bill_amt, bill_period=i_bill_period,
                  outputdiv=output_div)
        jp.Button(a=l_btn, text="generate PDF", click=cls.get_results, classes="bg-purple-700 rounded p-2 m-2",
                  fm1_name=i_fm1_name, fm2_name=i_fm2_name,
                  fm1_days=i_fm1_days, fm2_days=i_fm2_days,
                  bill_amt=i_bill_amt, bill_period=i_bill_period,
                  outputdiv=output_div)

        return wp

    @staticmethod
    def get_results(widget, msg):
        """
        calculates the bill amounts
        :param: widget is the widget which calls the function
        :return: none
        """

        the_bill = flat.Bill(float(widget.bill_amt.value), widget.bill_period.value)
        flatmate1 = flat.Flatmate(widget.fm1_name.value, float(widget.fm1_days.value))
        flatmate2 = flat.Flatmate(widget.fm2_name.value, float(widget.fm2_days.value))

        amount1 = flatmate1.pays(the_bill, flatmate2)
        amount2 = flatmate2.pays(the_bill, flatmate1)

        res_txt = f"{flatmate1.name} owes £{amount1:.2f}, {flatmate2.name} owes £{amount2:.2f}"

        widget.outputdiv.text = res_txt
