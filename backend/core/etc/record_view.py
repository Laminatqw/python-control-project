from django.utils.timezone import now

from apps.listing.models import ListingViewModel


def record_view(request, listing):
    viewer = request.user if request.user.is_authenticated else None
    ip_address = get_client_ip(request)

    print(f"Viewer: {viewer}, IP: {ip_address}, Listing ID: {listing.id}")  # Логування для перевірки

    # Перевірка унікальності перегляду за день
    if not ListingViewModel.objects.filter(
        listing=listing,
        viewer=viewer,
        ip_address=ip_address,
        viewed_at__date=now().date()
    ).exists():
        print(f"Creating new view record for listing {listing.id}")
        ListingViewModel.objects.create(
            listing=listing,
            viewer=viewer,
            ip_address=ip_address
        )

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(f"Extracted IP: {ip}")  # Перевірка отримання IP
    return ip
