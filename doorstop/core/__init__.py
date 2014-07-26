"""Core package for Doorstop."""

import logging

log = logging.Logger(__name__)  # pylint: disable=C0103

from doorstop.core.item import Item
from doorstop.core.document import Document
from doorstop.core.tree import Tree
from doorstop.core.builder import build, find_document, find_item
