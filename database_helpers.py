from sqlalchemy import Column, String, Integer, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel, Field, model_validator
from typing import Optional, List, Optional
from datetime import datetime
from enum import Enum

Base = declarative_base()

class ForeclosureCaseSchema(Base):
    __tablename__ = 'foreclosure_data'

    link = Column(String, nullable=False, primary_key=True)
    bundesland_code = Column(String, nullable=False)
    aktenzeichen = Column(String, nullable=False)
    letzte_aktualisierung = Column(String)
    art_der_versteigerung = Column(String)
    grundbuch = Column(String)
    objekt_lage = Column(String)
    beschreibung = Column(Text)
    verkehrswert = Column(String)
    termin = Column(Integer)
    ort_der_versteigerung = Column(String)
    amtliche_bekanntmachung = Column(String)
    exposee = Column(String)
    gutachten = Column(String)
    foto = Column(Text)

    objects = relationship("ForeclosureObjectSchema", back_populates="case", cascade="all, delete-orphan")

class ForeclosureObjectSchema(Base):
    __tablename__ = 'foreclosureobjects_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    foreclosurecase_link = Column(String, ForeignKey('foreclosure_data.link'), nullable=False)
    flaeche = Column(Integer, nullable=True)
    verkehrswert = Column(Integer, nullable=False)
    typ = Column(String, nullable=False)
    baujahr = Column(Integer, nullable=True)
    raeume = Column(Integer, nullable=True)
    raum_typen = Column(String, nullable=False)
    balkon = Column(Boolean, default=False)
    garten = Column(Boolean, default=False)
    
    case = relationship("ForeclosureCaseSchema", back_populates="objects")
    
class ForeclosureCaseModel(BaseModel):
    link: str
    aktenzeichen: str
    letzte_aktualisierung: int
    art_der_versteigerung: Optional[str] = None
    grundbuch: Optional[str] = None
    objekt_lage: Optional[str] = None
    beschreibung: Optional[str] = None
    verkehrswert: Optional[str] = Field(None, alias='verkehrswert_in_€')
    termin: Optional[int] = None
    ort_der_versteigerung: Optional[str] = None
    amtliche_bekanntmachung: Optional[str] = None
    exposee: Optional[str] = None
    gutachten: Optional[str] = None
    foto: Optional[str] = None

    class Config:
        populate_by_name = True

    @model_validator(mode='before')
    def convert_letzte_aktualisierung(cls, values):
        letzte_aktualisierung_str = values.get('letzte_aktualisierung')
        if letzte_aktualisierung_str and isinstance(letzte_aktualisierung_str, str):
            date_str = letzte_aktualisierung_str[1:-1].split(": ", 1)[1]
            date_obj = datetime.strptime(date_str, '%d-%m-%Y %H:%M')
            values['letzte_aktualisierung'] = int(date_obj.timestamp())
        return values

    @model_validator(mode='before')
    def convert_termin(cls, values):
        termin_str = values.get('termin')
        if termin_str and isinstance(termin_str, str):
            date_obj = datetime.strptime(termin_str, '%A, %d. %B %Y, %H:%M Uhr')
            values['termin'] = int(date_obj.timestamp())
        return values

    @model_validator(mode='before')
    def convert_fotos(cls, values):
        fotos_list = values.get('foto')
        if isinstance(fotos_list, list):
            values['foto'] = ','.join(fotos_list)
        return values

class Zustand(str, Enum):
    RENOVIERT = "Renoviert"
    NEU = "Neu"
    GEPFLEGT = "Gepflegt"
    
class Heizsystem(str, Enum):
    GAS = "Gas"
    STROM = "Strom"
    FERN = "Fernwärme"
    ÖL = "Öl"
    FESTBRENNSTOFFE = "Festbrennstoffe"

class RaumTyp(str, Enum):
    WOHNZIMMER = "Wohnzimmer"
    SCHLAFZIMMER = "Schlafzimmer"
    KUECHE = "Küche"
    BADEZIMMER = "Badezimmer"
    ARBEITSZIMMER = "Arbeitszimmer"
    HAUSWIRTSCHAFTSRAUM = "Hauswirtschaftsraum"
    FLUR = "Flur"
    ABSTELLRAUM = "Abstellraum"
    ESSZIMMER = "Esszimmer"

class VersteigerungsTyp(str, Enum):
    WOHNUNG = "Wohnung"
    HAUS = "Haus"
    ANDERES = "Anderes"

class ForclosureObjectModel(BaseModel):
    flaeche: int = Field(description="Die Fläche des Objekts in Quadratmetern.")
    verkehrswert: int = Field(description="Verkehrswert des Objekts.")
    typ: Optional[VersteigerungsTyp] = Field(description="Art der Immobilie (z.B. Wohnung, Haus oder etwas anderes).")
    baujahr: Optional[int] = Field(description="Baujahr der Immobilie.")
    raeume: Optional[int] = Field(description="Anzahl der Räume im Objekt.")
    raum_typen: List[RaumTyp] = Field(default_factory=list, description="""Liste der Raumtypen im Objekt (z.B. Wohnzimmer, Küche).
                                      Die Anzahl der Einträge in der Liste sollte der Gesamtzahl der Räume entsprechen. 
                                      Mehrere Räume desselben Typs sollten jeweils einzeln aufgeführt werden.""")
    balkon: bool = Field(description="Gibt an, ob das Objekt einen Balkon hat.")
    garten: bool = Field(description="Hat das Objekt einen Garten.")

class ForclosureModel(BaseModel):
    objekte: List[ForclosureObjectModel] = Field(description="Liste der Zwangsversteigerungsobjekte, die zu diesem Fall gehören.")
    gesamtverkehrswert: int = Field(description="Gesamtverkehrswert aller Zwangsversteigerungsobjekte.")

engine = create_engine('sqlite:///foreclosures.db')
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)