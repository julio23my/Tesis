# Generated by Django 2.2 on 2020-07-17 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200717_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segmento',
            name='mascara',
            field=models.CharField(choices=[('8', '255.0.0.0/8'), ('9', '255.128.0.0/9'), ('10', '255.192.0.0/10'), ('11', '255.224.0.0/11'), ('12', '255.240.0.0/12'), ('13', '255.248.0.0/13'), ('14', '255.252.0.0/14'), ('15', '255.254.0.0/15'), ('16', '255.255.0.0/16'), ('17', '255.255.128.0/17'), ('18', '255.255.192.0/18'), ('19', '255.255.224.0/19'), ('20', '255.255.240.0/20'), ('21', '255.255.248.0/21'), ('22', '255.255.252.0/22'), ('23', '255.255.254.0/23'), ('24', '255.255.255.0/24'), ('25', '255.255.255.128/25'), ('26', '255.255.255.192/26'), ('27', '255.255.255.224/27'), ('28', '255.255.255.240/28'), ('29', '255.255.255.248/29'), ('30', '255.255.255.252/30'), ('31', '255.255.255.254/31'), ('32', '255.255.255.255/32')], default='0', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='segmento',
            name='rango',
            field=models.CharField(default='0', max_length=50),
            preserve_default=False,
        ),
    ]
