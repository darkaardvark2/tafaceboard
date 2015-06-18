from django.db import models

from choices import *


class Subject(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/icons/', blank=True, null=True)

    is_ap = models.BooleanField(default=False)
    imageAP = models.ImageField(upload_to='images/icons/', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Tutor(models.Model):
    fname = models.CharField(max_length=255, blank=True)
    lname = models.CharField(max_length=255, blank=True)
    # Contact
    cell = models.CharField(max_length=255, blank=True)
    altphone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    altemail = models.CharField(max_length=255, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=255, blank=True)
    neighborhood = models.CharField(max_length=255, blank=True)
    hidden = models.BooleanField(default=False)
    # Bio
    gotofor = models.CharField(max_length=255, blank=True)
    highestLevel = models.CharField(max_length=255, blank=True)
    highestLevelManual = models.CharField(max_length=255, blank=True, choices=LEVEL)
    bioline1 = models.CharField(max_length=255, blank=True)
    bioline2 = models.CharField(max_length=255, blank=True)
    bioline3 = models.CharField(max_length=255, blank=True)
    bioline4 = models.CharField(max_length=255, blank=True)
    bioline5 = models.CharField(max_length=255, blank=True)
    # Descriptors
    gender = models.CharField(max_length=255, choices=GENDER, blank=True)
    area = models.CharField(max_length=255, choices=AREA, default=AREA[1][0], blank=True)
    availability = models.IntegerField(default=0, blank=True)
    availability_note = models.TextField(blank=True)
    availability_vacation = models.TextField(blank=True)
    availability_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    picture = models.ImageField(upload_to='images/', blank=True, null=True)

    def __unicode__(self):
        return self.fname

    class Meta:
        ordering = ('fname',)


class Capability(models.Model):
    level = models.CharField(max_length=255, choices=LEVEL, default='NO')
    level_note = models.TextField(blank=True)
    score = models.PositiveSmallIntegerField(default=0, blank=True)

    area = models.CharField(max_length=255, choices=AREA, blank=True, default="")
    notes = models.TextField(blank=True)

    subject = models.ForeignKey(Subject)
    tutor = models.ForeignKey(Tutor)

    def __unicode__(self):
        return self.tutor.fname + " - " + self.tutor.lname + " - " + self.subject.name

    class Meta:
        ordering = ('self.tutor.fname')

#
# End of Database Models
# 


# 
# View Models. These don't correspond with database tables. Only carry data from views to templates
#

class SubjectUpdate(models.Model):
    tutor_id = None
    subject = Subject()
    subject_form = ''
    capability = Capability()
    capability_form = ''
