# Generated by Django 4.2.4 on 2023-08-16 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.SmallIntegerField(default=0)),
                ('started_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('ends_on', models.DateTimeField(auto_now=True, null=True)),
                ('campaign_header_title', models.CharField(max_length=256)),
                ('campaign_header_category', models.CharField(max_length=100)),
                ('campaign_header_description', models.CharField(max_length=100)),
                ('campaign_status', models.SmallIntegerField(default=0)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'db_table': 'tbl_campaign_header',
            },
        ),
        migrations.CreateModel(
            name='CampaignInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('campaign_inquiry_type', models.CharField(max_length=10)),
                ('campaign_inquiry_content', models.CharField(max_length=10240)),
                ('campaign_inquiry_status', models.SmallIntegerField(default=0)),
                ('campaign_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaignheader')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'db_table': 'tbl_campaign_inquiry',
            },
        ),
        migrations.CreateModel(
            name='CampaignReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('campaign_review_title', models.CharField(max_length=50)),
                ('campaign_review_content', models.CharField(max_length=10240)),
                ('campaign_review_status', models.SmallIntegerField(default=0)),
                ('campaign_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaignheader')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'db_table': 'tbl_campaign_review',
            },
        ),
        migrations.CreateModel(
            name='CampaignPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('campaign_header_title', models.CharField(max_length=10)),
                ('campaign_detail_image', models.ImageField(null=True, upload_to='CampaignPhoto/%Y/%m/%d')),
                ('campaign_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaignheader')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'db_table': 'tbl_campaign_photo',
            },
        ),
        migrations.CreateModel(
            name='CampaignParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('campaign_participant_role', models.CharField(max_length=10)),
                ('campaign_participant_status', models.SmallIntegerField(default=0)),
                ('campaign_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaignheader')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'db_table': 'tbl_campaign_participant',
            },
        ),
        migrations.CreateModel(
            name='CampaignInquiryAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('campaign_inquiry_answer_content', models.CharField(max_length=1024)),
                ('campaign_inquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaigninquiry')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'db_table': 'tbl_campaign_inquiry_answer',
            },
        ),
        migrations.CreateModel(
            name='CampaignDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_detail_description1', models.CharField(max_length=256)),
                ('campaign_detail_description2', models.CharField(max_length=256)),
                ('campaign_detail_image', models.ImageField(upload_to='CampaignDetail/%Y/%m/%d')),
                ('campaign_detail_content', models.CharField(max_length=10240)),
                ('campaign_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaignheader')),
            ],
            options={
                'db_table': 'tbl_campaign_detail',
            },
        ),
    ]