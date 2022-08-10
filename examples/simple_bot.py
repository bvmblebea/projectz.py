import projectz

projectz = projectz.Client()
projectz.login(email="", password="")

projectz.send_message(p.get_joined_chats()["list"][0]["threadId"], "Welcome")

@p.on()
def event(data):
    projectz.send_message(data["msg"]["threadId"], f"Hello {data['author']['nickname']}")
