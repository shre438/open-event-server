from sqlalchemy.orm import backref

from app.models import db


class StripeAuthorization(db.Model):
    """
    Stripe authorization information for an event.
    """
    __tablename__ = 'stripe_authorizations'

    id = db.Column(db.Integer, primary_key=True)
    stripe_secret_key = db.Column(db.String)
    stripe_refresh_token = db.Column(db.String)
    stripe_publishable_key = db.Column(db.String)
    stripe_user_id = db.Column(db.String)
    stripe_email = db.Column(db.String)

    event_id = db.Column(db.Integer, db.ForeignKey('events.id', ondelete='CASCADE'))
    event = db.relationship('Event', backref=backref('stripe', uselist=False))

    def __init__(self,
                 stripe_secret_key=None,
                 stripe_refresh_token=None,
                 stripe_publishable_key=None,
                 stripe_user_id=None,
                 stripe_email=None,
                 event_id=None):
        self.stripe_secret_key = stripe_secret_key
        self.stripe_refresh_token = stripe_refresh_token
        self.stripe_publishable_key = stripe_publishable_key
        self.stripe_user_id = stripe_user_id
        self.stripe_email = stripe_email
        self.event_id = event_id

    def __repr__(self):
        return '<StripeAuthorization %r>' % self.stripe_user_id

    def __str__(self):
        return self.__repr__()

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'stripe_secret_key': self.stripe_secret_key,
            'stripe_refresh_token': self.stripe_refresh_token,
            'stripe_publishable_key': self.stripe_publishable_key,
            'stripe_user_id': self.stripe_user_id,
            'stripe_email': self.stripe_email
        }
