import reflex as rx
from chat.chat import index  # Import Reflex app page

# Create the app
app = rx.App()
app.add_page(index)

if __name__ == "__main__":
    app.compile()  # Correct method to build the appimport reflex as rx
from chat.chat import index  # Import the main Reflex app component

app = rx.App()
app.add_page(index)

if __name__ == "__main__":
    app.run()
