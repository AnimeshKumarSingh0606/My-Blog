

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogcomment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
