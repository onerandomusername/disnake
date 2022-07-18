# -*- encoding: utf-8 -*-

# original copyright notice as follows

# Copyright © 2012 New Dream Network, LLC (DreamHost)
#
# Author: Doug Hellmann <doug.hellmann@dreamhost.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# changes made:
# - added typehinting
# - formatted with black
# - removed `display_toc` being forced to True


from __future__ import annotations

from typing import TYPE_CHECKING

from sphinx import addnodes

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.builders.html import StandaloneHTMLBuilder
    from sphinx.environment import BuildEnvironment

GROUPED_SECTIONS = [("api", "api/index")]


def html_page_context(app: Sphinx, pagename: str, templatename, context, doctree):
    """Event handler for the html-page-context signal.
    Modifies the context directly.
     - Replaces the 'toc' value created by the HTML builder with one
       that shows all document titles and the local table of contents.
     - Sets display_toc to True so the table of contents is always
       displayed, even on empty pages.
     - Replaces the 'toctree' function with one that uses the entire
       document structure, ignores the maxdepth argument, and uses
       only prune and collapse.
    """
    # only work on grouped folders
    if not pagename.startswith(tuple(x[0] for x in GROUPED_SECTIONS)):
        return

    if "toctree" not in context:
        # json builder doesn't use toctree func, so nothing to replace
        return

    def make_toctree(collapse=True, maxdepth=-1, includehidden=True):
        return get_rendered_toctree(
            app.builder,  # type: ignore
            pagename,
            prune=False,
            collapse=collapse,
        )

    context["toctree"] = make_toctree


def get_rendered_toctree(builder: StandaloneHTMLBuilder, docname, prune=False, collapse=True):
    """Build the toctree relative to the named document,
    with the given parameters, and then return the rendered
    HTML fragment.
    """
    fulltoc = build_full_toctree(
        builder,
        docname,
        prune=prune,
        collapse=collapse,
    )
    rendered_toc = builder.render_partial(fulltoc)["fragment"]
    return rendered_toc


def build_full_toctree(builder: StandaloneHTMLBuilder, docname: str, prune: bool, collapse: bool):
    """Return a single toctree starting from docname containing all
    sub-document doctrees.
    """
    env: BuildEnvironment = builder.env  # type: ignore
    for name, index in GROUPED_SECTIONS:
        if docname.startswith(name):
            index = index
            break

    else:
        return
    doctree = env.get_doctree(index)
    toctrees = []
    for toctreenode in doctree.traverse(addnodes.toctree):
        toctree = env.resolve_toctree(
            docname,
            builder,
            toctreenode,
            collapse=collapse,
            prune=prune,
            includehidden=True,
        )
        if toctree is not None:
            toctrees.append(toctree)

    if not toctrees:
        return None
    result = toctrees[0]
    for toctree in toctrees[1:]:
        if toctree:
            result.extend(toctree.children)
    # env.resolve_references(result, docname, builder)
    return result


def setup(app: Sphinx):
    app.connect("html-page-context", html_page_context)
