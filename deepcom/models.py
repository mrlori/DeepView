from djongo import models
from django import forms


class ParticleData(models.Model):
  x = models.FloatField()
  y = models.FloatField()
  radius = models.FloatField()
  area = models.FloatField()
  class Meta:
    abstract = True

class ParticleDataForm(forms.ModelForm):
  class Meta:
    model = ParticleData
    fields = ('x', 'y', 'radius', 'area')

class Frame(models.Model):
  particles = models.ArrayField(
    model_container=ParticleData,
    model_form_class=ParticleDataForm,
  )

  class Meta:
    abstract = True

class FrameForm(forms.ModelForm):
  class Meta:
    model = Frame
    fields = ('particles',)


class VideoModel(models.Model):
  _id = models.ObjectIdField()
  created_at = models.DateTimeField(auto_created=True)
  video_path = models.CharField(max_length=255)
  frames = models.ArrayField(
    model_container=Frame,
    model_form_class=FrameForm,
    
  )

  objects = models.DjongoManager()
