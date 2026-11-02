from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .index import find


def health(request):
    return JsonResponse({"ok": True})


class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get("q", "")
        return Response({"query": query, "results": find(query)})
