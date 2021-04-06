

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200426_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
