from django.db import models
from user.models import User


class StudyPlan(models.Model):
    """
    学习计划表
    """
    sp_id = models.AutoField(primary_key=True)
    sp_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    sp_once_words = models.IntegerField()
    sp_once_sentences = models.IntegerField()
    sp_once_grammers = models.IntegerField()
    sp_other_settings = models.JSONField()
    class Meta:
        db_table = "study_plan"
