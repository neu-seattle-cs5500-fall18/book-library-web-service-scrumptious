from data_access_layer.book_copy_dao import BookCopyDao
from flask_restplus import abort
from model import db
from model.checkout import Checkout
from model.user import User


class CheckoutDao:

    @staticmethod
    def query_checkout(checkout_id):

        print('Query user')
        a_checkout = Checkout.query.get(checkout_id)

        if a_checkout is None:
            abort(400, 'Record not found')
        else:
            return a_checkout.to_dict()

    @staticmethod
    def get_all_checkouts():
        print('Get all checkouts')

        list_of_checkouts = []
        query_results = Checkout.query.all()

        for checkout in query_results:
            list_of_checkouts.append(checkout.to_dict())
        return list_of_checkouts

    @staticmethod
    def create_new_checkout(checkout_dict):

        new_checkout = Checkout(**checkout_dict)
        book_copy_id = new_checkout.book_copy_id
        book_copy = BookCopyDao.get_book_copy(book_copy_id)
        book_copy.is_checked_out = True

        db.session.add(new_checkout)
        db.session.commit()
        print('checkout created')

        return new_checkout.checkout_id

    @staticmethod
    def get_checkout(checkout_id):

        print('Get a checkout')

        a_checkout = Checkout.query.get(checkout_id)

        return a_checkout.to_dict

    @staticmethod
    def update(checkout_id, checkout_info_dict):

        print('Updating checkout')
        a_checkout = Checkout.query.get(checkout_id)
        book_copy_id = a_checkout.book_copy_id
        book_copy = BookCopyDao.get_book_copy(book_copy_id)
        book_copy.is_checked_out = False
        a_checkout.update(**checkout_info_dict)
        db.session.commit()
        return a_checkout.to_dict()

    @staticmethod
    def delete_checkout(checkout_id):

        print('Delete checkout')

        a_checkout = Checkout.query.filter_by(checkout_id=checkout_id).delete()
        db.session.commit()
        return a_checkout

    @staticmethod
    def joint_to_dict(checkout_id, user_id, book_id, book_copy_id, checkout_date, due_date, return_date,
                      user_first_name, user_last_name, user_email):
        joint_dict = {
            'checkout_id': checkout_id,
            'user_id': user_id,
            'book_id': book_id,
            'book_copy_id': book_copy_id,
            'checkout_date': checkout_date,
            'due_date': due_date,
            'return_date': return_date,
            'user_first_name': user_first_name,
            'user_last_name': user_last_name,
            'user_email': user_email,
        }
        return joint_dict

    @staticmethod
    def get_reminders():
        list_of_checkouts = []
        # userList = users.query.join(friendships, users.id == friendships.user_id)
        # .add_columns(users.userId, users.name, users.email, friends.userId, friendId).filter(
        #     users.id == friendships.friend_id).filter(friendships.user_id == userID).paginate(page, 1, False)
        results = db.session.query(Checkout).join(Book).join(User)
        # results = Checkout.query.join(User, Checkout.user_id == User.user_id).add_columns(Checkout.checkout_id,
        #                                                                                   Checkout.user_id,
        #                                                                                   Checkout.book_id,
        #                                                                                   Checkout.book_copy_id,
        #                                                                                   User.user_first_name,
        #                                                                                   User.user_last_name,
        #                                                                                   Checkout.due_date,
        #                                                                                   Checkout.return_date,
        #                                                                                   User.email)\
        #     .filter(Checkout.return_date is None, User.user_id == Checkout.user_id)


        results = results.filter(Checkout.return_date is None)

        print(results)
        results.all()

        for checkout in results:
            list_of_checkouts.append(checkout.joint_to_dict)
        return list_of_checkouts





