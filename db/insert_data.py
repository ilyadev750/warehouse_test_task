from sqlalchemy.orm import Session
from models import Category, MainShelve, Good, MinorShelve
from engine import engine


with Session(engine) as session:
    m_shelve_1 = MinorShelve(name='Б', good_id=2)
    m_shelve_2 = MinorShelve(name='5', good_id=2)
    m_shelve_3 = MinorShelve(name='А', good_id=4)
    m_shelve_4 = MinorShelve(name='10', good_id=4)
    m_shelve_5 = MinorShelve(name='ж', good_id=7)
    
    session.add_all([m_shelve_1, m_shelve_2, m_shelve_3, m_shelve_4, m_shelve_5])
    session.commit()