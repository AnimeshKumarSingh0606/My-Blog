

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogComment'),
        ),
    ]
