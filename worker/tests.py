from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *


class WorkerModelTestCase(TestCase):
    def test_create_worker(self):
        user = User.objects.create(username='test_user')
        worker = Worker.objects.create(
            user=user,
            name='test',
            specialization='Dev',
            expected_salary=5000,
            is_searching=True
        )

        self.assertEqual(worker.name, 'test')
        self.assertEqual(worker.specialization, 'Dev')
        self.assertEqual(worker.expected_salary, 5000)
        self.assertTrue(worker.is_searching)


class ResumeModelTestCase(TestCase):
    def test_create_resume(self):
        user = User.objects.create(username='test_user')
        worker = Worker.objects.create(user=user, name='test', specialization='Dev', expected_salary=5000)
        resume = Resume.objects.create(
            name=worker,
            age=25,
            specialization='Web Developer',
            info='Тестовая информация о резюме'
        )

        self.assertEqual(resume.name, worker)
        self.assertEqual(resume.age, 25)
        self.assertEqual(resume.specialization, 'Web Developer')
        self.assertEqual(resume.info, 'Тестовая информация о резюме')


class CommentModelTestCase(TestCase):
    def test_create_comment(self):
        user = User.objects.create(username='test_user')
        worker = Worker.objects.create(user=user, name='test', specialization='Dev', expected_salary=5000)
        comment = Comment.objects.create(
            text='Тестовый комментарий',
            worker=worker,
            author=user
        )

        self.assertEqual(comment.text, 'Тестовый комментарий')
        self.assertEqual(comment.worker, worker)
        self.assertEqual(comment.author, user)

    # Дополнительно: проверка ImageField
    def test_resume_image_field(self):
        user = User.objects.create(username='test_user')
        worker = Worker.objects.create(user=user, name='test', specialization='Dev', expected_salary=5000)
        resume = Resume.objects.create(
            name=worker,
            age=25,
            specialization='Web Developer',
            info='Тестовая информация о резюме'
        )

        # Создаем тестовое изображение с расширением jpg
        image = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        resume.profile_photo = image
        resume.save()

        self.assertEqual(resume.profile_photo.url, f'/media/{resume.profile_photo.name}')
