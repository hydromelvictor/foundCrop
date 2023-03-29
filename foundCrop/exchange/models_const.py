"""_summary_
"""
# ----------------------------------------------------------------------------

from exchange.constant import CATEGORY
from exchange.models import Client, Command, Product, Professional, User


USERS = User.objects.all()
PROFESSIONAL_USERS = Professional.objects.filter(is_prof=True)
CLIENT_USERS = Client.objects.filter(is_client=True)

CMD = Command.objects.all()