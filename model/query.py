from model import db

# component --> Objeto al que hace referencia (anode, cathode, thermal)
def data_extraction(component, query_conditions):

    db.Base.metadata.create_all(db.engine)

    if(query_conditions.get('origin')!= None and query_conditions.get('manuforiented') != None):
        ob = db.session.query(component).filter(component.origin == query_conditions.get('origin')).\
            filter(component.manuforiented == query_conditions.get('manuforiented')).all()
    elif(query_conditions.get('origin')!= None):
        ob = db.session.query(component).filter(component.origin == query_conditions.get('origin')).all()
    elif(query_conditions.get('manuforiented') != None):
        ob = db.session.query(component).filter(component.manuforiented == query_conditions.get('manuforiented')).all()
    else:
        ob = db.session.query(component).all()

    return ob

# component --> Objeto al que hace referencia (anode, cathode, thermal)
def labels(component, query_conditions):

    db.Base.metadata.create_all(db.engine)
    db_labels = db.session.query(component.label).filter(component.origin == query_conditions.get('origin')). \
        filter(component.manuforiented == query_conditions.get('manuforiented')).group_by(component.label)

    if (query_conditions.get('origin') != None and query_conditions.get('manuforiented') != None):
        db_labels = db.session.query(component.label).filter(component.origin == query_conditions.get('origin')). \
            filter(component.manuforiented == query_conditions.get('manuforiented')).group_by(component.label)

    elif (query_conditions.get('origin') != None):
        db_labels = db.session.query(component.label).filter(component.origin == query_conditions.get('origin')).\
            group_by(component.label)

    elif (query_conditions.get('manuforiented') != None):
        db_labels = db.session.query(component.label).filter(component.origin == query_conditions.get('manuforiented')).\
            group_by(component.label)

    else:
        db_labels = db.session.query(component.label).group_by(component.label)

    extracted_labels = []
    for label in db_labels:
        extracted_labels.append(label.label)

    return extracted_labels