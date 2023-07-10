from prefect import flow, task

@task
def create_message():
    msg = "this is my test task"
    return msg

@flow
def test_flow():
    task_message = create_message()
    print(task_message)


if __name__ == "__main__":
    test_flow()
