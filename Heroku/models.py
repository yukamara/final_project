def create_classes(db):
    class Amazon(db.Model):
        __tablename__ = 'amazon'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64))
        lat = db.Column(db.Float)
        lon = db.Column(db.Float)

        def __repr__(self):
            return '<Amazon %r>' % (self.name)
    return Amazon
