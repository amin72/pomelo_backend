from django.db import models


# Create your models here.
class Point(models.Model):
    altitude = models.CharField(max_length=255, null=True, blank=True)
    anemometer_alive = models.CharField(max_length=255, null=True, blank=True)
    awdir_geo = models.CharField(max_length=255, null=True, blank=True)
    aws_internet  = models.CharField(max_length=255, null=True, blank=True)
    aws_q_size  = models.CharField(max_length=255, null=True, blank=True)
    aws_sent_payloads  = models.CharField(max_length=255, null=True, blank=True)
    aws_timeouts  = models.CharField(max_length=255, null=True, blank=True)
    aws_uprate  = models.CharField(max_length=255, null=True, blank=True)
    ch4_advection  = models.CharField(max_length=255, null=True, blank=True)
    ch4_alive  = models.CharField(max_length=255, null=True, blank=True)
    ch4_ch4d  = models.CharField(max_length=255, null=True, blank=True)
    ch4_diag  = models.CharField(max_length=255, null=True, blank=True)
    ch4_droprate  = models.CharField(max_length=255, null=True, blank=True)
    ch4_epochtime  = models.CharField(max_length=255, null=True, blank=True)
    ch4_errorcode  = models.CharField(max_length=255, null=True, blank=True)
    ch4_milliseconds  = models.CharField(max_length=255, null=True, blank=True)
    ch4_moleratio  = models.CharField(max_length=255, null=True, blank=True)
    ch4_mr_anomaly  = models.CharField(max_length=255, null=True, blank=True)
    ch4_mr_delayed  = models.CharField(max_length=255, null=True, blank=True)
    ch4_mr_mean  = models.CharField(max_length=255, null=True, blank=True)
    ch4_mr_median  = models.CharField(max_length=255, null=True, blank=True)
    ch4_mr_sd  = models.CharField(max_length=255, null=True, blank=True)
    ch4_nanoseconds  = models.CharField(max_length=255, null=True, blank=True)
    ch4_plume  = models.CharField(max_length=255, null=True, blank=True)
    ch4_pressure  = models.CharField(max_length=255, null=True, blank=True)
    ch4_qc  = models.CharField(max_length=255, null=True, blank=True)
    ch4_recordtime  = models.DateTimeField(null=True, blank=True)
    ch4_rssi  = models.CharField(max_length=255, null=True, blank=True)
    ch4_rssi_sd  = models.CharField(max_length=255, null=True, blank=True)
    ch4_temp  = models.CharField(max_length=255, null=True, blank=True)
    closest_fenced_site = models.CharField(max_length=255, null=True, blank=True)
    computer_time  = models.DateTimeField(max_length=255, null=True, blank=True)
    dead_reckoning  = models.CharField(max_length=255, null=True, blank=True)
    dt_logger_alive  = models.CharField(max_length=255, null=True, blank=True)
    estimated_heading  = models.CharField(max_length=255, null=True, blank=True)
    fence_status  = models.CharField(max_length=255, null=True, blank=True)
    frame  = models.CharField(max_length=255, null=True, blank=True)
    geo_sep  = models.CharField(max_length=255, null=True, blank=True)
    gps_alive  = models.CharField(max_length=255, null=True, blank=True)
    gps_fix  = models.CharField(max_length=255, null=True, blank=True)
    gps_time_ori  = models.TimeField(null=True, blank=True)
    gps_time_pos  = models.TimeField(null=True, blank=True)
    heading  = models.CharField(max_length=255, null=True, blank=True)
    heading_available  = models.CharField(max_length=255, null=True, blank=True)
    horizontal_dil  = models.CharField(max_length=255, null=True, blank=True)
    hpr_type  = models.CharField(max_length=255, null=True, blank=True)
    latitude  = models.FloatField()
    lgr_alive  = models.CharField(max_length=255, null=True, blank=True)
    log_time  = models.CharField(max_length=255, null=True, blank=True)
    longitude  = models.FloatField()
    note  = models.CharField(max_length=255, null=True, blank=True)
    num_sats  = models.CharField(max_length=255, null=True, blank=True)
    par_frame  = models.CharField(max_length=255, null=True, blank=True)
    pitch  = models.CharField(max_length=255, null=True, blank=True)
    public_IP  = models.CharField(max_length=255, null=True, blank=True)
    ref_station_id  = models.CharField(max_length=255, null=True, blank=True)
    rm_young_86000_alive  = models.CharField(max_length=255, null=True, blank=True)
    rmys_record_time  = models.DateTimeField(null=True, blank=True)
    rmys_sonictemp  = models.CharField(max_length=255, null=True, blank=True)
    rmys_status  = models.CharField(max_length=255, null=True, blank=True)
    rmys_wdir_cf  = models.CharField(max_length=255, null=True, blank=True)
    rmys_wspd2D_cf  = models.CharField(max_length=255, null=True, blank=True)
    rmys_wspd3D_cf  = models.CharField(max_length=255, null=True, blank=True)
    roll  = models.CharField(max_length=255, null=True, blank=True)
    spd_over_grnd  = models.CharField(max_length=255, null=True, blank=True)
    speed_mean  = models.CharField(max_length=255, null=True, blank=True)
    status_nominal  = models.CharField(max_length=255, null=True, blank=True)
    system_id  = models.CharField(max_length=255, null=True, blank=True)
    track_mean  = models.CharField(max_length=255, null=True, blank=True)
    track_turn_rate  = models.CharField(max_length=255, null=True, blank=True)
    track_turn_rate_filtered  = models.CharField(max_length=255, null=True, blank=True)
    travel_az  = models.CharField(max_length=255, null=True, blank=True)
    travel_speed  = models.CharField(max_length=255, null=True, blank=True)
    true_track  = models.CharField(max_length=255, null=True, blank=True)
    true_wdir  = models.CharField(max_length=255, null=True, blank=True)
    true_wspd  = models.CharField(max_length=255, null=True, blank=True)
    utm_zone = models.CharField(max_length=255, null=True, blank=True)
    wdir_cf_corrected  = models.CharField(max_length=255, null=True, blank=True)
    wspd_cf_corrected = models.CharField(max_length=255, null=True, blank=True)
    x_utm = models.CharField(max_length=255, null=True, blank=True)
    y_utm = models.CharField(max_length=255, null=True, blank=True)
    latest_gps_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'({self.latitude}, {self.longitude})'
