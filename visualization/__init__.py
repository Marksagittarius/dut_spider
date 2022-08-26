from .actress import render_all_about_actress
from .television import render_all_about_television
from .epidemic import render_all_about_epidemic


def render_all():
    """ Render all the webview.
    """
    render_all_about_actress()
    render_all_about_television()
    render_all_about_epidemic()
    
    