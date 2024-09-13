from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        editor_group, created = Group.objects.get_or_create(name='Editors')
        if created:
            permissions = Permission.objects.filter(
            )
            editor_group.permissions.set(permissions)
            self.stdout.write(self.style.SUCCESS('Successfully created "Editors" group with specified permissions.'))
        else:
            self.stdout.write(self.style.WARNING('"Editors" group already exists.'))
