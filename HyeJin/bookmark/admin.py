from django.contrib import admin
from bookmark.models import Bookmark #[주의] ch99. 제거

# Register your models here.
@admin.register(Bookmark) # Bookmark 테이블을 등록
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url','content') # 보여줄 컬럼 지정