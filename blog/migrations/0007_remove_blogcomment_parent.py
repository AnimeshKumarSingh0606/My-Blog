

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200425_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='parent',
        ),
    ]
