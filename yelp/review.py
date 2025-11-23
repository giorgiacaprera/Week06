from dataclasses import dataclass
from datetime import datetime

# from yelp.business import Business
# from yelp.business import User

@dataclass
class Review:
    review_id: str
    business_id: str # Oppure:
    # business : Business
    user_id: str #Oppure:
    # user : User
    stars: float
    review_date: datetime.date #str
    votes_funny: int
    votes_useful: int
    votes_cool: int
    review_text: str

    def __str__(self):
        return self.review_id+" "+self.business_id+" "+self.user_id+" "+str(self.stars)+" "+str(self.review_date)+" "+str(self.votes_funny)+" "+str(self.votes_useful)+" "+str(self.votes_cool)+" "+self.review_text

    def __eq__(self, other):
        return self.review_id==other.review_id

    def __hash__(self):
        return hash(self.review_id)