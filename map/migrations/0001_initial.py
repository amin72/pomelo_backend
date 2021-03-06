# Generated by Django 4.0.1 on 2022-01-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altitude', models.CharField(blank=True, max_length=255, null=True)),
                ('anemometer_alive', models.CharField(blank=True, max_length=255, null=True)),
                ('awdir_geo', models.CharField(blank=True, max_length=255, null=True)),
                ('aws_internet', models.CharField(blank=True, max_length=255, null=True)),
                ('aws_q_size', models.CharField(blank=True, max_length=255, null=True)),
                ('aws_sent_payloads', models.CharField(blank=True, max_length=255, null=True)),
                ('aws_timeouts', models.CharField(blank=True, max_length=255, null=True)),
                ('aws_uprate', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_advection', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_alive', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_ch4d', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_diag', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_droprate', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_epochtime', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_errorcode', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_milliseconds', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_moleratio', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_mr_anomaly', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_mr_delayed', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_mr_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_mr_median', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_mr_sd', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_nanoseconds', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_plume', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_pressure', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_qc', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_recordtime', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_rssi', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_rssi_sd', models.CharField(blank=True, max_length=255, null=True)),
                ('ch4_temp', models.CharField(blank=True, max_length=255, null=True)),
                ('closest_fenced_site', models.CharField(blank=True, max_length=255, null=True)),
                ('computer_time', models.CharField(blank=True, max_length=255, null=True)),
                ('dead_reckoning', models.CharField(blank=True, max_length=255, null=True)),
                ('dt_logger_alive', models.CharField(blank=True, max_length=255, null=True)),
                ('estimated_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('fence_status', models.CharField(blank=True, max_length=255, null=True)),
                ('frame', models.CharField(blank=True, max_length=255, null=True)),
                ('geo_sep', models.CharField(blank=True, max_length=255, null=True)),
                ('gps_alive', models.CharField(blank=True, max_length=255, null=True)),
                ('gps_fix', models.CharField(blank=True, max_length=255, null=True)),
                ('gps_time_ori', models.CharField(blank=True, max_length=255, null=True)),
                ('gps_time_pos', models.CharField(blank=True, max_length=255, null=True)),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('heading_available', models.CharField(blank=True, max_length=255, null=True)),
                ('horizontal_dil', models.CharField(blank=True, max_length=255, null=True)),
                ('hpr_type', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.FloatField()),
                ('lgr_alive', models.CharField(blank=True, max_length=255, null=True)),
                ('log_time', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.FloatField()),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('num_sats', models.CharField(blank=True, max_length=255, null=True)),
                ('par_frame', models.CharField(blank=True, max_length=255, null=True)),
                ('pitch', models.CharField(blank=True, max_length=255, null=True)),
                ('public_IP', models.CharField(blank=True, max_length=255, null=True)),
                ('ref_station_id', models.CharField(blank=True, max_length=255, null=True)),
                ('rm_young_86000_alive', models.CharField(blank=True, max_length=255, null=True)),
                ('rmys_record_time', models.CharField(blank=True, max_length=255, null=True)),
                ('rmys_sonictemp', models.CharField(blank=True, max_length=255, null=True)),
                ('rmys_status', models.CharField(blank=True, max_length=255, null=True)),
                ('rmys_wdir_cf', models.CharField(blank=True, max_length=255, null=True)),
                ('rmys_wspd2D_cf', models.CharField(blank=True, max_length=255, null=True)),
                ('rmys_wspd3D_cf', models.CharField(blank=True, max_length=255, null=True)),
                ('roll', models.CharField(blank=True, max_length=255, null=True)),
                ('spd_over_grnd', models.CharField(blank=True, max_length=255, null=True)),
                ('speed_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('status_nominal', models.CharField(blank=True, max_length=255, null=True)),
                ('system_id', models.CharField(blank=True, max_length=255, null=True)),
                ('track_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('track_turn_rate', models.CharField(blank=True, max_length=255, null=True)),
                ('track_turn_rate_filtered', models.CharField(blank=True, max_length=255, null=True)),
                ('travel_az', models.CharField(blank=True, max_length=255, null=True)),
                ('travel_speed', models.CharField(blank=True, max_length=255, null=True)),
                ('true_track', models.CharField(blank=True, max_length=255, null=True)),
                ('true_wdir', models.CharField(blank=True, max_length=255, null=True)),
                ('true_wspd', models.CharField(blank=True, max_length=255, null=True)),
                ('utm_zone', models.CharField(blank=True, max_length=255, null=True)),
                ('wdir_cf_corrected', models.CharField(blank=True, max_length=255, null=True)),
                ('wspd_cf_corrected', models.CharField(blank=True, max_length=255, null=True)),
                ('x_utm', models.CharField(blank=True, max_length=255, null=True)),
                ('y_utm', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
