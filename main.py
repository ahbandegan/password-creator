from flet import *
from random import randint

def main(page: Page):

    l_AZ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    l_az = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    l_09 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    l_more = ["@", "_", "-", ".", "(", ")", "&", "!", "?"]

    def _create(e):
        if not A_Z.value and not a_z.value and not _0_9.value and not more.value and length.value == "" or length.value == "0":
            alert_text.value = "please selection customize for create password"

        else:
            help = []
            result = ""

            if A_Z.value:
                help += l_AZ
            if a_z.value:
                help += l_az
            if _0_9.value:
                help += l_09
            if more.value:
                help += l_more

            for i in range(int(length.value)):
                result += help[randint(0, len(help) - 1)]

            page.set_clipboard(result)

            alert_text.value = "password created and copied to clipboard"

        alert.open = True
        page.update()

    custom = Card(
        content=Column(
            [
                Row(
                    [
                        A_Z := Checkbox(label="A_Z"),
                        a_z := Checkbox(label="a_z"),
                        _0_9:= Checkbox(label="0_9"),
                        more:= Checkbox(label="more"),
                    ], 'center'
                ),
                Row(
                    [
                        length := TextField(
                            label="length",
                            hint_text="0",
                            width=100,
                            keyboard_type=KeyboardType.NUMBER,
                            text_align=TextAlign.CENTER,
                        ),
                    ], 'center'
                )
            ], 'center'
        ),
        height=120
    )
    create = Container(
        content=Row(
            [
                img := Image(
                    src="lock.png",
                    width=300,
                    height=300,
                )
            ]
        ),
        width=img.width + 20,
        height=img.height + 20,
        on_click=_create,
        ink=True,
        border_radius=30
    )
    alert_text = Text(color="white")
    alert = SnackBar(
        content=Row(
            [
                alert_text
            ], alignment='center'
        ),
        bgcolor="#666666",
    )

    page.window.width = 350
    page.window.height = 550
    page.overlay.append(alert)
    page.add(
        custom,
        create
    )


if __name__ == '__main__':
    app(main)
