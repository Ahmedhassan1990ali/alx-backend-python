from rest_framework.pagination import PageNumberPagination

class MessagePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        """Returns paginated response with count via page.paginator.count"""
        response = super().get_paginated_response(data)
        response.data['total_items'] = self.page.paginator.count
        return response