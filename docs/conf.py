from typing import List

import zoloto

project = "Zoloto"
copyright = "2020, Jake Howard"  # noqa: A001
author = "Jake Howard"

release = zoloto.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
    "m2r",
]

templates_path = []  # type: List[str]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "cv2": (
        "https://docs.opencv.org/3.0-last-rst/",
        None,
    ),  # This is the most recent version with intersphinx support.
    "numpy": ("https://docs.scipy.org/doc/numpy", None),
}

html_theme = "sphinx_rtd_theme"

html_static_path = []  # type: List[str]

autodoc_default_options = {
    "member-order": "alphabetical",
    "special-members": "__init__, __iter__",
    "undoc-members": True,
    "inherited-members": True,
}

autodoc_mock_imports = ["picamera"]
