from django.db import models


class Interaction(models.Model):
    input = models.CharField(max_length=100)
    output = models.TextField()
    script = models.TextField()
    execute_script = models.BooleanField(default=False)

    def __unicode__(self):
        return self.input

    def get_outpu(self, binds):
        return self.output % binds

    def execute(self):
        try:
            exec(self.script)
            dic = script()
            return dic
        except Exception as ex:
            return 'ERRO', str(ex)

    class Meta:
        db_table = 'interaction'
