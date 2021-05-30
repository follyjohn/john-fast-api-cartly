from sqlalchemy.orm import Session


from ..model import Categorie as CategorieModel
from ..schema import categorie as CategorieShema


def get_categorie(db: Session, categorie_id: int):
    return db.query(CategorieModel).filter(CategorieModel.id == categorie_id).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CategorieModel).offset(skip).limit(limit).all()


def create_categorie(db: Session, categorie: CategorieShema.CategorieCreate):
    db_categorie = CategorieModel(
        slug=categorie.slug, name=categorie.name)
    db.add(db_categorie)
    db.commit()
    db.refresh(db_categorie)
    return db_categorie
