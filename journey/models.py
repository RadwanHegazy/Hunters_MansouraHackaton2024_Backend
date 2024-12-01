from django.db import models
from users.models import User

class Journey (models.Model) : 
    driver = models.ForeignKey(User, related_name='journey_driver', on_delete=models.CASCADE)
    riders = models.ManyToManyField(User, related_name='riders_driver', null=True, blank=True)

    from_place = models.CharField(max_length=225)
    to_place = models.CharField(max_length=225)
    start_at = models.DateTimeField()

    def get_journyes(self, from_, to_) : 
        return Journey.objects.filter(
            to_palce=to_,
            from_place=from_
        )
    
    def __str__(self) -> str:
        return f'{self.from_place} -> {self.to_place}'

