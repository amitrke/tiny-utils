from atlassian import Confluence
import commonutils

def connect(url: str, token: str) -> Confluence:
    """Returns a connection to Confluence"""
    confluence = Confluence(
        url=url,
        token=token
    )
    return confluence

def get_page_by_id(confluence: Confluence, page_id: str) -> dict:
    """Returns a page by ID"""
    page = confluence.get_page_by_id(
        page_id=page_id,
        expand='body.storage'
    )
    return page