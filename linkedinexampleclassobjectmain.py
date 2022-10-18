import linkedinexampleclassobject
from linkedinexampleclassobjectpost import Post

app_user_one=linkedinexampleclassobject.User("a@s.com","poorvi","devops engg","123456")
app_user_one.get_user_info()
app_user_one.change_role("devops")
app_user_one.get_user_info()


new_post=Post("I am learning python",app_user_one.name)
new_post.showpost()