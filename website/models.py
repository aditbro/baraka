from django.db import models
from djrichtextfield.models import RichTextField

long_text = 800
short_text = 20

# Create your models here.
class LowonganKerja(models.Model):
    DAERAH_CHOICES = [
        ('JKT', 'Jakarta'),
        ('JABAR', 'Jawa Barat'),
        ('JATENG', 'Jawa Tengah'),
        ('JATIM', 'Jawa Timur')
    ]
    daerah = models.CharField(max_length=short_text, choices=DAERAH_CHOICES)
    posisi = models.CharField(max_length=long_text)
    kota = models.CharField(max_length=short_text)
    jenis = models.CharField(max_length=short_text)
    persyaratan = RichTextField(field_settings='advanced')
    tanggung_jawab = RichTextField(field_settings='advanced')

    def __str__(self):
        return self.posisi + " " + self.kota
    
    class Meta:
        verbose_name_plural = "Lowongan Kerja"

class DataBarang(models.Model):
    pengirim = models.CharField(max_length=short_text)
    dari = models.CharField(max_length=short_text)
    tujuan = models.CharField(max_length=short_text)
    lokasi = models.CharField(max_length=short_text)
    status = models.CharField(max_length=short_text)

    def __str__(self):
        return ("Data Barang")
    
    class Meta:
        verbose_name_plural = "Data Barang"