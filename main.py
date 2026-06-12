import flet as ft

def main(page: ft.Page):
    # Set the app title and center the content alignment
    page.title = "Flet Android Test App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Define UI UI Text Element
    title_text = ft.Text(
        value="Flet CI/CD Success!", 
        size=30, 
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_ACCENT
    )
    
    status_text = ft.Text(
        value="Type something below to test interactivity:", 
        size=16
    )

    # Input Field
    user_input = ft.TextField(
        label="Your Name", 
        width=300,
        text_align=ft.TextAlign.CENTER
    )

    # Button Click Event Handler
    def on_button_click(e):
        if user_input.value:
            status_text.value = f"Hello, {user_input.value}! Your app works perfectly."
        else:
            status_text.value = "Please enter a name first!"
        page.update()

    # Submit Button
    submit_btn = ft.ElevatedButton(
        text="Greet Me", 
        on_click=on_button_click,
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLUE_ACCENT,
        )
    )

    # Add all elements to the application view
    page.add(
        title_text,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        status_text,
        user_input,
        submit_btn
    )

# Target target determines if it runs as a desktop app or gets web/mobile wrapper
ft.app(target=main)
  
