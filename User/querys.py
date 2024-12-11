# from User.models import Administrator
#
#
# def QueryShowDoctorSamespecializations(user):
#     return Administrator.objects.filter(
#         Organization=user.administrator.Organization,
#         DoctorSpecializations__in=user.administrator.DoctorSpecializations.all()
#     ).distinct()
#
# def QueryShowAllAdmin(user):
#     return Administrator.objects.filter(Organization=user.administrator.Organization)