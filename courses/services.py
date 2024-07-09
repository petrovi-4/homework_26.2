from django.conf import settings
from django.core.mail import send_mail

from config.settings import STRIPE_SECRET_KEY
import stripe

from courses.models import Subscription


def get_a_link_to_pay_for_the_course(course):

    stripe.api_key = STRIPE_SECRET_KEY

    product = stripe.Product.create(name=course.title)

    price = stripe.Price.create(
        unit_amount=course.price,
        currency="usd",
        recurring={"interval": "month"},
        product=product.id,
    )

    payment_link = stripe.PaymentLink.create(
        line_items=[
            {
                "price": price.id,
                "quantity": 1,
            },
        ],
    )

    return payment_link.url


def send_mailing(subscription_pk):
    """
    Отправляет пользователю письмо об обновлении материалов курса, на который он подписан
    :param subscription_pk: id подпискu на обновление курса
    :return: None
    """
    subscription = Subscription.objects.get(pk=subscription_pk)
    user = subscription.user
    emails = [user.email]
    course = subscription.course

    send_mail(
        subject="Обновление курса",
        message=f"Курс {course.title} обновлен",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails
    )