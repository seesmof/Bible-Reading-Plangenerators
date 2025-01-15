from dataclasses import dataclass

@dataclass(frozen=True)
class Language:
    EN='English'
    UK='Ukrainian'
    DE='German'

@dataclass(frozen=True)
class LinkType:
    MDE='Markdown External'
    MDI='Markdown Internal'
    HTML='HTML'
    NO='None'

@dataclass(frozen=True)
class LinkSource:
    BOLLS='Bolls Life'
    EBIBLE='eBible.org'
    YOUVERSION='YouVersion'
    BLB='Blue Letter Bible'

@dataclass(frozen=True)
class LinkBase:
    LinkSource.BOLLS='https://bolls.life'
    LinkSource.EBIBLE='https://ebible.org/study/?w1=bible&t1=local%3A'

