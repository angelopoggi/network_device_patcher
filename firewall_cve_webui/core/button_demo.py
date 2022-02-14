from pglet import Stack, Text, Button, Message

class DemoButon:
    def __init__(self,action):
        self.action = self.button_action()
    def button_action(self):
        def button_clicked_message():
            return Stack(
                width="70%",
                gap=20,
                controls=[
                    Message(value="all your base are belong to us"),
            ]
            )
        return Stack(
            horizontal=True,
            controls=[
                Button(icon="U+26B0",
                       title="Patch",
                       on_click=button_clicked_message()
                       ),
            ],
        )