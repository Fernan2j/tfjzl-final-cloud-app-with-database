from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# --- Inline Classes ---

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# --- Admin Classes with Decorators ---

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content', 'course', 'grade']
    list_filter = ['course']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# No custom configuration:
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    pass

@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    pass

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    pass