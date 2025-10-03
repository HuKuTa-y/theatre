from dataclasses import dataclass
from typing import Optional

@dataclass
class Category:
    id: Optional[int] = None
    name: str = ""
    content: str = ""
    

@dataclass
class Subsections:
    id: Optional[int] = None
    name: str = ""
    content: str = ""
    link: str = ""

@dataclass
class Source:
    id: Optional[int] = None
    name: str = ""
    link: str = ""

@dataclass
class Users:
    id: Optional[int] = None
    name: str = ""
    id_chat: Optional[int] = None