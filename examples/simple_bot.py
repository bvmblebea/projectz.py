import projz

ProjectZ = projz.Client()
ProjectZ.login("", "")

ProjectZ.send_message(p.get_joined_chats()["list"][0]["threadId"], "Welcome")

@p.on()
def event(data):
    ProjectZ.send_message(data["msg"]["threadId"], f"Hello {data['author']['nickname']}")
