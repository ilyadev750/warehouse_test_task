from db.engine import engine
from db.models import Base


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print('Success!')