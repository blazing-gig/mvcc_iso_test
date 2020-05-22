from django.db import transaction
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Account
import time
# Create your views here.

class SampleView(APIView):


    # def get(self, request):
    #     with transaction.atomic():
    #         sleep = request.query_params.get("sleep")
    #
    #         p1 = int(request.query_params["p1"])
    #         p2 = int(request.query_params["p2"])
    #
    #         s = Sample.objects.get(id = 1)
    #
    #         print("data before is ", {"num": s.num, "num_2": s.num_2}, " sleep ", sleep)
    #
    #         s.num -= p1
    #         s.num_2 += p2
    #         s.save()
    #
    #         # print("data after is ", {"num": s.num, "num_2": s.num_2}, " sleep ", sleep)
    #         # # time.sleep(int(sleep))
    #         #
    #         # # s2 = Sample.objects.get(id = 1)
    #         #
    #         # print("final data is ", {"num": s2.num, "num_2": s2.num_2}, " sleep ", sleep)
    #
    #     return Response(data = {"num": s.num, "num_2": s.num_2})

    # def get(self, request):
    #     with transaction.atomic():
    #         s = Sample.objects.get(id = 1)
    #         s1 = Sample_1.objects.get(id = 1)
    #     return Response(data = {"num": s.num, "balance": s1.balance})

    def put(self, request):
        with transaction.atomic():
            qs = list(
                Account.objects.select_for_update().filter(id__in = [1, 2]).order_by('id')
            )

            acc_to_debit = qs[0]
            acc_to_credit = qs[1]

            amount_to_debit = request.data["amount_to_debit"]

            acc_to_debit.balance -= amount_to_debit
            acc_to_credit.balance += amount_to_debit
            acc_to_debit.save()
            acc_to_credit.save()

        return Response(data = {})

    def post(self, request):
        with transaction.atomic():
            amount_to_debit = request.data["amount_to_debit"]
            Account.objects.filter(id = 1).update(
                balance = F('balance') - amount_to_debit
            )
            Account.objects.filter(id = 2).update(
                balance = F('balance') + amount_to_debit
            )
        return Response(data = {})


    # def put(self, request):
    #     with transaction.atomic():
    #         s = Sample.objects.select_for_update().filter(id = 1)[0]
    #         s1 = Sample_1.objects.select_for_update().filter(id = 1)[0]
    #
    #         p1 = int(request.query_params["p1"])
    #         p2 = int(request.query_params["p2"])
    #
    #         s.num -= p1
    #         s1.balance += p2
    #         s.save()
    #         s1.save()
    #     return Response(data = {})

    # def post(self, request):
    #     with transaction.atomic():
    #         # sleep = request.query_params["sleep"]
    #
    #         p1 = int(request.query_params["p1"])
    #         p2 = int(request.query_params["p2"])
    #
    #         # print("data before is ", {"num": s.num, "num_2": s.num_2}, " sleep ", sleep)
    #         Sample_1.objects.filter(balance = 1000).update(
    #             balance = F('balance') + p2
    #         )
    #
    #         # Sample.objects.filter(id = 1).update(
    #         #     num = F('num') - p1
    #         # )
    #
    #
    #         # s.num -= p1
    #         # s.num_2 += p2
    #         # s.save()
    #
    #         # print("data after is ", {"num": s.num, "num_2": s.num_2}, " sleep ", sleep)
    #     # time.sleep(int(sleep))
    #
    #     # s2 = Sample.objects.get(id = 1)
    #
    #     # print("final data is ", {"num": s2.num, "num_2": s2.num_2}, " sleep ", sleep)
    #
    #     return Response({})


    # def delete(self, request):
    #     # import time
    #     # time.sleep(0.02)
    #     with transaction.atomic():
    #         p1 = int(request.query_params["p1"])
    #         p2 = int(request.query_params["p2"])
    #
    #         Sample_1.objects.filter(balance = 1000).delete()
    #
    #     return Response({})





