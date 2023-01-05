from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, User, Message, MessageThread
from app.forms.message_form import MessageForm
from .auth_routes import validation_errors_to_error_messages


chat_routes = Blueprint("chat", __name__)


# GET CURRENT USER'S CHAT THREADS
@chat_routes.route('')
@login_required
def get_chat_threads():
    """
    Get chat threads of current user
    """

    user = User.query.get(current_user.get_id())
    user_chats = user.user_chats

    return {"Chats": [thread.to_dict() for thread in user_chats]}


# GET ONE CHAT BY ID
@chat_routes.route('/<int:id>')
@login_required
def get_one_chat(id):
    """
    Get one chat thread by its ID
    """

    chat = MessageThread.query.get(id)

    return {"Chat": chat.to_dict()}


# CREATE NEW MESSAGE THREAD BETWEEN CURR USER AND TARGET USER
@chat_routes.route('', methods=["POST"])
@login_required
def create_thread():
    """
    Create a new message thread between the current user and a selected user
    """

    currUser = User.query.get(current_user.get_id())
    targetUser = User.query.get(request.json["targetUserId"])

    new_thread = MessageThread()
    currUser.user_chats.append(new_thread)
    targetUser.user_chats.append(new_thread)
    db.session.add(new_thread)
    db.session.commit()

    return {"message": "Thread successfully created", "status_code": 200}


# ADD A MESSAGE TO A THREAD BY ITS ID
@chat_routes.route('/<int:id>', methods=["POST"])
@login_required
def add_message(id):
    """
    Add message to a chat thread by its ID
    """

    form = MessageForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        data = form.data

        new_msg = Message(
            message=data["body"],
            user_id=current_user.get_id(),
            message_thread_id=id
        )

        db.session.add(new_msg)
        db.session.commit()

        return new_msg.to_dict()
    return {"errors": validation_errors_to_error_messages(form.errors)}, 403


# DELETE A THREAD BY ITS ID
@chat_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_thread(id):
    """
    Delete a thread by its ID
    """

    thread = MessageThread.query.get(id)
    db.session.delete(thread)
    db.session.commit()
    return {"message": "Successfully deleted", "status_code": 200}


# DELETE A MESSAGE BY ITS ID
@chat_routes.route('/message/<int:id>', methods=["DELETE"])
@login_required
def delete_message(id):
    """
    Delete a message by its ID
    """

    message = Message.query.get(id)
    db.session.delete(message)
    db.session.commit()
    return {"message": "Successfully deleted", "status_code": 200}

# # ADD A LIKE TO A POST BY POST ID
# @likes_routes.route("/<int:id>", methods=["POST"])
# @login_required
# def add_like(id):
#     """
#     A logged-in user can add a like to any post by its ID.
#     """

#     user = User.query.get(current_user.get_id())
#     post = Post.query.get(id)
#     user.user_likes.append(post)

#     db.session.commit()

#     return {"message": "successfully liked post"}


# # REMOVE A LIKE FROM A POST BY POST ID
# @likes_routes.route("/<int:id>", methods=["DELETE"])
# @login_required
# def remove_like(id):
#     """
#     A logged-in user can remove a like from any post by its ID.
#     """

#     user = User.query.get(current_user.get_id())
#     post = Post.query.get(id)
#     user.user_likes.remove(post)

#     db.session.commit()

#     return {"message": "successfully unliked post"}