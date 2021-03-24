from django.conf.urls import url
from django.urls import path
from . import views

app_name = "Profile"

urlpatterns = [
    path("account_status/", views.index, name = "account_status"),
    path("edit_detail/", views.edit_detail, name = "edit_detail"),
    path("settings/",views.settings,name="settings"),
    path("delete_account/",views.delete_account,name="delete_account"),
    path("money_transfer/", views.money_transfer, name = "money_transfer"),
    path("loan_app/", views.loan, name = "loan_app"),
    path("ewallet/", views.ewallet, name = "ewallet"),
    path("online_pay/", views.online_pay, name = "online_pay"),
    # path("deposit/", views.DepositMoney, name="deposit_money"),
    # path("withdraw/", views.WithdrawMoney, name="withdraw_money"),
    




]
