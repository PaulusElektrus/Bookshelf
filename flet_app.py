import flet
from flet import Page
from book.BookApp import BookApp

def main(page: Page):
    page.title = "Bookshelf App"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.update()

    # create application instance
    app = BookApp()

    # add application's root control to the page
    page.add(app)

if __name__ == "__main__":
    flet.app(target=main)