from django.views.generic import TemplateView
from datetime import date
import random


visitor_name="鈴木"

# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["visitor"] = visitor_name

        return ctxt


class AboutView(TemplateView):
    template_name='about.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["my_name"] = "武田"
        ctxt["birth_day"] = date(1994, 1, 27)
        ctxt["commbat_power"] = 530000
        ctxt["skills"] = [
            "指先からの気功波",
            "光線眼",
            "爆発波",
            "超能力"
        ]
        ctxt["defeat_enemy"] = [
            "デンデ",
            "クリリン",
            "ベジータ"
        ]
        ctxt["visitor"] = visitor_name
        ctxt["rondomint"] =random.randint(0,2)
        return ctxt
