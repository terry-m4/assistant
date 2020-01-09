from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Journal
from django.contrib.auth.mixins import LoginRequiredMixin

# 日誌列表
class JournalList(LoginRequiredMixin, ListView):
    model = Journal
    ordering = ['-id']      # 依 id 欄位反向排序(新的在前面)
    paginate_by = 3         # 設定每頁最多顯示的資料筆數

# 新增日誌
class JournalCreate(CreateView):
    model = Journal
    fields = ['content']            
    success_url = '/journal/'      
    template_name = 'form.html'

# 修改日誌
class JournalUpdate(UpdateView):
    model = Journal
    fields = ['content']  
    success_url = '/journal/' 
    template_name = 'form.html'

# 刪除日誌
class JournalDelete(DeleteView):
    model = Journal
    success_url = '/journal/'      
    template_name = 'confirm_delete.html'