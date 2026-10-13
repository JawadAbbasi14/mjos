from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="detail_content",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]