# Generated by Django 2.2.6 on 2020-12-30 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gud_app', '0006_remove_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_order',
            field=models.ManyToManyField(related_name='products_order', to='gud_app.Order'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.CharField(max_length=45)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='gud_app.Product')),
            ],
        ),
    ]
