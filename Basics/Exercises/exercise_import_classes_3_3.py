# 03.08.2017
from exercise_import_classes_3_2 import Admin

admin_privileges = ('can add post', 'can delete post', 'can ban user')
admin_1 = Admin(admin_privileges)
admin_1.privileges.show_privileges()
