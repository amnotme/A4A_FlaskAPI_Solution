from dataclasses import dataclass
from typing import Optional


@dataclass
class Player:
    playerID: str
    birthYear: Optional[int]
    birthMonth: Optional[int]
    birthDay: Optional[int]
    birthCountry: Optional[str]
    birthState: Optional[str]
    birthCity: Optional[str]
    deathYear: Optional[int]
    deathMonth: Optional[int]
    deathDay: Optional[int]
    deathCountry: Optional[str]
    deathState: Optional[str]
    deathCity: Optional[str]
    nameFirst: Optional[str]
    nameLast: Optional[str]
    nameGiven: Optional[str]
    weight: Optional[int]
    height: Optional[int]
    bats: Optional[str]
    throws: Optional[str]
    debut: Optional[str]
    finalGame: Optional[str]
    retroID: Optional[str]
    bbrefID: Optional[str]
