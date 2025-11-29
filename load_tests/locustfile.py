from locust import HttpUser, task, between

class LoadTestingUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def health(self):
        self.client.get("/healthcheck")

    @task
    def predict(self):
        # простое тело запроса
        self.client.post("/predict", json={"x": 10})
