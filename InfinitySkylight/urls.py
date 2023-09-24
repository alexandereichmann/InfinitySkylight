from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Users import views as user
from Operating import views as Operating
from Maintenance import views as Maintenance
from Chemical import views as Chemical

router = DefaultRouter()
router.register('user', user.Userviewset)
router.register('LastOperatingvalues', Operating.LastOperatingvaluesviewset)
router.register('GT11', Operating.Gt11viewset)
router.register('GT12', Operating.Gt12viewset)
router.register('ST10', Operating.St10viewset)
router.register('RW1', Operating.Rw1viewset)
router.register('DW1', Operating.Dw1viewset)
router.register('Vacuum1', Operating.Vacuum1viewset)
router.register('TrancT1', Operating.TrancT1viewset)
router.register('GasP1', Operating.GasP1viewset)
router.register('GT21', Operating.Gt21viewset)
router.register('GT22', Operating.Gt22viewset)
router.register('ST20', Operating.St20viewset)
router.register('RW2', Operating.Rw2viewset)
router.register('DW2', Operating.Dw2viewset)
router.register('Vacuum2', Operating.Vacuum2viewset)
router.register('TrancT2', Operating.TrancT2viewset)
router.register('GasP2', Operating.GasP2viewset)
router.register('IC', Maintenance.ICviewset)
router.register('Elec', Maintenance.Elecviewset)
router.register('Mech', Maintenance.Mechviewset)
router.register('LastChemicalvalues', Chemical.LastChemicalvaluesviewset)
router.register('HPD11', Chemical.HPD11viewset)
router.register('IPD11', Chemical.IPD11viewset)
router.register('LPD11', Chemical.LPD11viewset)
router.register('HPMS11', Chemical.HPMS11viewset)
router.register('IPMS11', Chemical.IPMS11viewset)
router.register('LPMS11', Chemical.LPMS11viewset)
router.register('HPD12', Chemical.HPD12viewset)
router.register('IPD12', Chemical.IPD12viewset)
router.register('LPD12', Chemical.LPD12viewset)
router.register('HPMS12', Chemical.HPMS12viewset)
router.register('IPMS12', Chemical.IPMS12viewset)
router.register('LPMS12', Chemical.LPMS12viewset)
router.register('HPD21', Chemical.HPD21viewset)
router.register('IPD21', Chemical.IPD21viewset)
router.register('LPD21', Chemical.LPD21viewset)
router.register('HPMS21', Chemical.HPMS21viewset)
router.register('IPMS21', Chemical.IPMS21viewset)
router.register('LPMS21', Chemical.LPMS21viewset)
router.register('HPD22', Chemical.HPD22viewset)
router.register('IPD22', Chemical.IPD22viewset)
router.register('LPD22', Chemical.LPD22viewset)
router.register('HPMS22', Chemical.HPMS22viewset)
router.register('IPMS22', Chemical.IPMS22viewset)
router.register('LPMS22', Chemical.LPMS22viewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
