import apscheduler
from pytz import utc
print(dir(apscheduler))
import logging
from sqlalchemy import create_engine
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler,BlockingScheduler

from apscheduler.jobstores.base import BaseJobStore, JobLookupError, ConflictingIdError
from apscheduler.util import maybe_ref, datetime_to_utc_timestamp, utc_timestamp_to_datetime
from apscheduler.job import Job
from apscheduler import *
logging.basicConfig()
res=logging.getLogger('apscheduler').setLevel(logging.DEBUG)
res1=logging.getLogger('apscheduler').setLevel(logging.INFO)

# engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/jobstore')
# print (engine)
# mysql_engine = create_engine('mysql://ravi:teja@123@:{3}'.format('ravi', 'teja@123', 'http://127.0.0.1/teja', '3306'))

jobstores = {
        'default': SQLAlchemyJobStore(url='postgresql+psycopg2://postgres:admin@localhost')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 1,
    'misfire_grace_time':1200
}

sched = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)

sched.add_job(build, 'date', run_date=time,id=link+" "+str(uniqueid),max_instances=1,replace_existing=True,args=x)
sched.start()


# engine = create_engine(db_uri)
