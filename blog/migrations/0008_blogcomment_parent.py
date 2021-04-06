

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_blogcomment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogComment'),
        ),
    ]
