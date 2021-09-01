from marko.block import Heading
from marko.parser import Parser
import re


def get_href(heading):
    """
    Description
    -----------

    Get the markdown href from a heading string.

    Parameters
    ----------

    heading : str
        Heading string content

    Returns
    -------

    href: str
        href pointing to the heading

    Examples
    --------

    >>> get_href("This is My Heading !")
    '#this-is-my-heading-'

    >>> get_href("This is My Heading with an emoji ! :fire:")
    '#this-is-my-heading-with-an-emoji-'
    """
    href = heading.lower()
    href = re.sub(r":\w+:", "", href)
    href = "#" + re.sub(r"[^A-Za-z0-9\-\s]+", "", href)
    href = re.sub(r"\s+", "-", href)
    return href


def get_toc(markdown_content, min_depth=None, max_depth=None):
    """
    Description
    -----------

    Return the table of contents in markdown format, from markdown content.

    Parameters
    ----------

    markdown_content: str
        Markdown content. Is typically the content of a readme.md file. It can
        contain a table of contents.

    min_depth: int or None
        Minimum heading level. If this is set to `None`, there is no minimum
        depth applied. For example, if you set min_depth to `2`, all the
        headings with level < 2 will be ignored (such as "# Dummy Heading").

        Defaults to `None`

    min_depth: int or None
        Maximum heading level. If this is set to `None`, there is no minimum
        depth applied. For example, if you set max_depth to `3`, all the
        headings with level > 3 will be ignored (such as "#### Dummy Heading").

        Defaults to `None`

    Returns
    -------

    toc : str
        String content of the table of contents, in markdown format
    """
    p = Parser()
    parsed = p.parse(markdown_content)
    toc = ""

    # Get all the heading elements
    for child in parsed.children:
        if isinstance(child, Heading):
            if min_depth is None or child.level >= min_depth:
                if max_depth is None or child.level <= max_depth:
                    toc += "\t" * (child.level - 1) + f"* [{child.children[0].children}]({get_href(child.children[0].children)})\n"
    return toc


def generate_toc(markdown_content, toc_title="Table of Contents", toc_level=2, min_depth=None, max_depth=None):
    """
    Description
    -----------

    Generate a table of contents for the markdown content, replacing the old
    table of contents if it exists.

    Parameters
    ----------

    markdown_content: str
        Markdown content. Is typically the content of a readme.md file. It can
        contain a table of contents.

    min_depth: int or None
        Minimum heading level. If this is set to `None`, there is no minimum
        depth applied. For example, if you set min_depth to `2`, all the
        headings with level < 2 will be ignored (such as "# Dummy Heading").

        Defaults to `None`

    min_depth: int or None
        Maximum heading level. If this is set to `None`, there is no minimum
        depth applied. For example, if you set max_depth to `3`, all the
        headings with level > 3 will be ignored (such as "#### Dummy Heading").

        Defaults to `None`

    Returns
    -------

    toc : str
        String content of the table of contents, in markdown format
    """

    toc = get_toc(markdown_content, min_depth, max_depth)

    # If the toc is empty, nothing is added
    if toc == '':
        return markdown_content

    # No table of contents in the file
    if "[](mdtoc)" not in markdown_content or "[](/mdtoc)" not in markdown_content:
        lines = markdown_content.split('\n')
        lines.insert(0, "[](mdtoc)\n# " + toc_title + "\n\n" + toc + "[](/mdtoc)\n")
        return '\n'.join(lines)
    else:
        return re.sub(r"(?<=\[]\(mdtoc\)).*(?=\[]\(/mdtoc\))", "\n" + "#" * toc_level + " " + toc_title + "\n\n" + toc, markdown_content, flags=re.DOTALL)