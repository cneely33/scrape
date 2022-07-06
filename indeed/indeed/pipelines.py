

from sqlalchemy.orm import sessionmaker
from indeed.models import Jobs, db_connect, create_jobs_table


class IndeedPipeline(object):
    """Indeed pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates jobs table.
        """
        engine = db_connect()
        create_jobs_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        
        session = self.Session()
        job = Jobs(**item)

        try:
            session.add(job)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item