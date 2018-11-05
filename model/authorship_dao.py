from model.book import authorship


def create_authorship(book_id, author_id_list):

    for author in author_id_list:
        authorship.insert(book_id=book_id, author_id=author)
    return #???


# this creates a list of author book key value pairs.
def get_authorship(**kwargs):
    authorship_list = []
    query_results = authorship.query.filter_by(**kwargs)

    for result in query_results:
        authorship_list.append(result)
    return


# what are the args here?
def delete_authorship(**kwargs):
    return


