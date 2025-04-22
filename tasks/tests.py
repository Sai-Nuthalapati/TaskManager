from rest_framework.test import APITestCase
from rest_framework import status
from tasks.models import Task

class TaskForkTestCase(APITestCase):
    def setUp(self):
        self.original_task = Task.objects.create(
            name="Test Task",
            description="Fork me",
            status="running"
        )

    def test_fork_task(self):
        url = f'/tasks/{self.original_task.id}/fork/'
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data['id'], self.original_task.id)
        self.assertIn("copy", response.data['name'])
        self.assertEqual(response.data['description'], self.original_task.description)
        self.assertEqual(response.data['status'], self.original_task.status)

        self.assertEqual(Task.objects.count(), 2)
