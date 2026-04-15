from rest_framework import permissions


class IsVipSpaAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # ১. ইউজারকে অবশ্যই লগইন করা থাকতে হবে
        if not request.user or not request.user.is_authenticated:
            return False

        # ২. সুপার ইউজার হলে সব এক্সেস পাবে
        if request.user.is_superuser:
            return True

        # ৩. ইউজার যদি 'VipSpa' গ্রুপের মেম্বার হয়, তবেই এক্সেস পাবে
        return request.user.groups.filter(name="VipSpa").exists()
