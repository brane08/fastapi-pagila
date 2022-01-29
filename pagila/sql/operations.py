from typing import List

from sqlalchemy.orm import Session

from sql import models
from sql.models import Actor


def get_actors(db: Session, page: int, size: int) -> List[Actor]:
    return db.query(models.Actor).offset(((page - 1) * size)).limit(size).all()


def get_actor(db: Session, actor_id: int) -> Actor:
    return db.query(models.Actor).filter(models.Actor.id == actor_id).first()
