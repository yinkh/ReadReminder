from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
import logging

logger = logging.getLogger("info")


class ChapterListViewView(LoginRequiredMixin, ListView):
    model = Chapter
    paginate_by = 12
    template_name = 'reminder/list.html'
    raise_exception = True


class ChapterDetailView(LoginRequiredMixin, DetailView):
    model = Chapter
    template_name = 'reminder/detail.html'
    slug_field = 'id'
    raise_exception = True

    def get_context_data(self, **kwargs):
        queryset = self.get_queryset()
        chapter = self.get_object()
        # 计算上一页、下一页
        queryset_list = list(queryset)
        for index in range(0, len(queryset_list)):
            if chapter == queryset_list[index]:
                kwargs['chapter_next'] = queryset_list[index + 1] if index + 1 < len(queryset_list) else None
                kwargs['chapter_previous'] = queryset_list[index - 1] if index - 1 >= 0 else None
        return super(ChapterDetailView, self).get_context_data(**kwargs)
