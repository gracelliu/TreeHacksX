import reflex as rx


class MicIcon(rx.Component):
    def __init__(self, icon_name, **props):
        super().__init__(**props)
        self.icon_name = icon_name

    def render(self):
        # Assuming you have the SVG code for the icon saved as a string
        icon_svg = self.get_icon_svg(self.icon_name)
        return rx.raw_html(icon_svg)

    def get_icon_svg(self, icon_name):
        # Replace this with the actual method to retrieve the SVG code
        # This could be from a local file, an API, or any other source
        return "<svg>...</svg>"
