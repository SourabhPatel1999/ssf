import streamlit as st
import pymongo
#
# import hashlib
#
#
# def make_hashes(password):
#     return hashlib.sha256(str.encode(password)).hexdigest()
#
#
# def check_hashes(password, hashed_text):
#     if make_hashes(password) == hashed_text:
#         return hashed_text
#     return False
#
# client = pymongo.MongoClient(
#     'mongodb+srv://user1:3N7AkEaDqXCgKr2w@cluster0.fdq4e.mongodb.net/?retryWrites=true&w=majority'
# )
#
# if 'user_name' not in st.session_state:
#     st.session_state['user_name'] = 'aaa'
# if 'login' not in st.session_state:
#     st.session_state['login'] = False
# if 'showbooks' not in st.session_state:
#     st.session_state['showbooks'] = False
#
#
# db = client.get_database('main').user1
# dbCart = client.get_database('cart').books
# ratingDB = client.get_database('cart').rate
#
# def add_userdata(username, password):
#     record = {
#         'username' : username,
#         'password' : password
#     }
#     db.insert_one(record)
#
# def valid_user(username, password):
#     record = {
#         'username': username,
#         'password': password
#     }
#     if (db.count_documents(record, limit = 1))>=1:
#         return True
#     else:
#         return False
#
# def user_name_available(username):
#     if (db.count_documents({'username':username}, limit = 1))<1:
#         return True
#     else:
#         return False
#
# def fun():
#     input = st.text_input("Enter Book name")
#     print(input)
#     if st.button("Add to Cart"):
#         record = {
#             'username': st.session_state['user_name'],
#             'book': input
#         }
#         dbCart.insert_one(record)
#
#     if st.button("Show all books")  :
#         for x in dbCart.find({'username':st.session_state['user_name']}):
#             st.write(x["book"])
#
#
# def main():
#     """Simple Login App"""
#
#     # print(st.session_state['user_name'])
#
#     st.title("Simple Login App")
#
#     book = "book1"
#     rating = st.number_input("Rate the book?", min_value=-5, max_value=+5, value=0, step=1)
#     ratingDB.insert_one({
#         'username': st.session_state['username'],
#         'book':book,
#         'rating':rating
#     })
#
#     menu = ["Login", "SignUp"]
#     choice = st.sidebar.selectbox("Menu", menu)
#
#     if st.session_state['login']:
#         fun()
#     elif choice == "Login":
#         st.subheader("Login Section")
#
#         username = st.text_input("User Name")
#         password = st.text_input("Password", type='password')
#         if st.button("Login"):
#             result = valid_user(username, make_hashes(password))
#             if result:
#                 st.session_state['login'] = True
#                 st.session_state['user_name'] = username
#                 st.success("Logged In as {}".format(username))
#
#                 task = st.selectbox("Task", ["Add Post", "Analytics", "Profiles"])
#                 if task == "Add Post":
#                     st.subheader("Add Your Post")
#
#                 elif task == "Analytics":
#                     st.subheader("Analytics")
#                 elif task == "Profiles":
#                     st.subheader("User Profiles")
#
#                 fun()
#
#             else:
#                 st.warning("Incorrect Username/Password")
#
#
#     elif choice == "SignUp":
#         st.subheader("Create New Account")
#         new_user = st.text_input("Username")
#         unique_username = user_name_available(new_user)
#         if not unique_username:
#             st.warning("Username taken, please select a new Username")
#         new_password = st.text_input("Password", type='password')
#
#         # if not unique_username:
#         #     st.warning("Username taken, please select a new Username")
#
#         if st.button("Signup"):
#             if (new_user == '') or (new_password == ''):
#                 st.warning("Some fields missing")
#
#             else:
#                 add_userdata(new_user, make_hashes(new_password))
#                 st.success("You have successfully created a valid Account")
#                 st.info("Go to Login Menu to login")
#
#     # print(st.session_state['user_name'])
#
#
# if __name__ == '__main__':
# 	main()