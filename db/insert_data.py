from sqlalchemy.orm import Session
from models import Category
from engine import engine


with Session(engine) as session:
    laptop = Category(category="Ноутбук",)
    monitor = Category(category="Монитор",)
    system_block = Category(category="Системный блок")
    clocks = Category(category="Часы")
    microphone = Category(category="Микрофон")

    # session.add_all([laptop, monitor, system_block, clocks, microphone])
    session.add_all([laptop])
    session.commit()
