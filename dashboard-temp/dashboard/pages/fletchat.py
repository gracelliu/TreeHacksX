import flet as ft

def main(page: ft.Page):
    page.title = "Flet Chat"

    # subscribe to broadcast messages
    def on_message(msg):
        messages.controls.append(ft.Text(msg))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(f"{user.value}: {message.value}")
        # clean up the form
        message.value = ""
        page.update()

    messages = ft.Column(scroll="AUTO")
    user = ft.TextField(hint_text="Your name", width=150, bgcolor="#aae6cd")
    message = ft.TextField(hint_text="Your message...", expand=True, bgcolor="#aae6cd")  # fill all the space
    send = ft.ElevatedButton("Send", on_click=send_click, bgcolor="#4EB389", color="#ffffff")
    page.add(messages, ft.Row(controls=[user, message, send]))

ft.app(target=main, view=ft.AppView.WEB_BROWSER)