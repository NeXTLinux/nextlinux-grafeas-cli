from nextlinux_engine import db
from nextlinux_engine.db import Nextlinux


# for the Nextlinux class/table

def get(session=None):
    if not session:
        session = db.Session

    ret = {}

    result = session.query(Nextlinux).first()

    if result:
        obj = dict((key,value) for key, value in vars(result).iteritems() if not key.startswith('_'))
        ret = obj

    return(ret)

def add(service_version, db_version, inobj, session=None):
    if not session:
        session = db.Session

    #our_result = session.query(Nextlinux).filter_by(service_version=service_version, db_version=db_version).first()
    our_result = session.query(Nextlinux).first()
    if not our_result:
        new_service = Nextlinux(service_version=service_version, db_version=db_version)
        new_service.update(inobj)

        session.add(new_service)
    else:
        inobj['service_version'] = service_version
        inobj['db_version'] = db_version
        our_result.update(inobj)

#    try:
#        session.commit()
#    except Exception as err:
#        raise err
#    finally:
#        session.rollback()
    
    return(True)

def update(service_version, db_version, scanner_version, inobj, session=None):
    return(add(service_version, db_version, scanner_version, inobj, session=session))

