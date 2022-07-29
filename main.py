import flet
from flet import ElevatedButton, Text, TextField
from login import login


def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        elif login(txt_name.value, txt_pass.value):
            name = txt_name.value
            page.clean()
            page.add(Text(f"Hello, {name} Login Successfully!"))
        else:
            name = txt_name.value
            page.clean()
            page.add(Text(f"{name} is Not Registered"))

    txt_name = TextField(label="Please Enter Your email To Login")
    txt_pass = TextField(label="Please Enter Your Password", password=True)

    page.add(txt_name, txt_pass, ElevatedButton("Login !!", on_click=btn_click))


flet.app(target=main)
