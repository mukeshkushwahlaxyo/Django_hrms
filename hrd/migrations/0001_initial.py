from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicsMast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doman_of_study', models.CharField(max_length=50, null=True)),
                ('name_of_board', models.CharField(max_length=50, null=True)),
                ('complete_in', models.DateField(null=True)),
                ('gared', models.CharField(max_length=10, null=True)),
                ('document', models.CharField(max_length=255, null=True)),
                ('note', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accou_hol_name', models.CharField(max_length=255, null=True)),
                ('accou_num', models.CharField(max_length=255, null=True)),
                ('bank_name', models.CharField(max_length=255, null=True)),
                ('ifsc_code', models.FloatField(null=True)),
                ('branch', models.CharField(max_length=255, null=True)),
                ('document', models.CharField(max_length=255, null=True)),
                ('note', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComapnyMast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DesigMast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_title', models.CharField(max_length=255, null=True)),
                ('document_status', models.CharField(max_length=55, null=True)),
                ('note', models.TextField(null=True)),
                ('files', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True)),
                ('reports_to', models.IntegerField(null=True)),
                ('emp_code', models.IntegerField(null=True)),
                ('comp_id', models.IntegerField(null=True)),
                ('dept_id', models.IntegerField(null=True)),
                ('desg_id', models.IntegerField(null=True)),
                ('grade_id', models.IntegerField(null=True)),
                ('emp_name', models.CharField(max_length=255, null=True)),
                ('emp_img', models.TextField(null=True)),
                ('emp_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('emp_dob', models.DateField(null=True)),
                ('curr_addr', models.TextField(null=True)),
                ('perm_addr', models.TextField(null=True)),
                ('blood_grp', models.CharField(max_length=5, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('alt_contact', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('driv_lic', models.CharField(max_length=255, null=True)),
                ('aadhar_no', models.CharField(max_length=25, null=True)),
                ('voter_id', models.CharField(max_length=50, null=True)),
                ('pan_no', models.CharField(max_length=50, null=True)),
                ('emp_type', models.IntegerField(null=True)),
                ('emp_status', models.IntegerField(null=True)),
                ('old_uan', models.CharField(max_length=50, null=True)),
                ('curr_uan', models.CharField(max_length=50, null=True)),
                ('old_pf', models.CharField(max_length=50, null=True)),
                ('curr_pf', models.CharField(max_length=50, null=True)),
                ('old_esi', models.CharField(max_length=50, null=True)),
                ('curr_esi', models.CharField(max_length=50, null=True)),
                ('join_dt', models.DateField(null=True)),
                ('leave_dt', models.DateField(null=True)),
                ('active', models.IntegerField(null=True)),
                ('leave_allotted', models.IntegerField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, null=True)),
                ('job_type', models.CharField(max_length=255, null=True)),
                ('designation', models.CharField(max_length=255, null=True)),
                ('monthly_ctc', models.FloatField(null=True)),
                ('comp_loc', models.CharField(max_length=255, null=True)),
                ('comp_email', models.CharField(max_length=255, null=True)),
                ('comp_doc', models.CharField(max_length=255, null=True)),
                ('join_date', models.DateField(null=True)),
                ('leave_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GradesMast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusMast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypesMast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
