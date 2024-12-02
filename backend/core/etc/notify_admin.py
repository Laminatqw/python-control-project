from django.core.mail import send_mail


def notify_admin_about_new_brand(user, brand):
    send_mail(
        subject="New car brand request",
        message=f"User {user.email} requests to add the brand: {brand}.",
        from_email="no-reply@platform.com",
        recipient_list=["admin@platform.com"],
    )