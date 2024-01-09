from atlassian import Confluence
import commonutils

def connect(url: str, token: str) -> Confluence:
    """Returns a connection to Confluence"""
    confluence = Confluence(
        url=url,
        token=token
    )
    return confluence

def get_page_by_title(confluence: Confluence, space: str, title: str) -> dict:
    """Returns a page by title"""
    page = confluence.get_page_by_title(
        space=space,
        title=title,
        expand='body.storage'
    )
    return page

def get_pages_by_space(confluence: Confluence, space: str, limit: int = 500) -> dict:
    """Returns a list of pages in a space"""
    pages = confluence.get_all_pages_from_space(
        space=space,
        start=0,
        limit=limit,
        expand='body.storage'
    )
    return pages

def get_page_by_id(confluence: Confluence, page_id: str) -> dict:
    """Returns a page by ID"""
    page = confluence.get_page_by_id(
        page_id=page_id,
        expand='body.storage'
    )
    return page