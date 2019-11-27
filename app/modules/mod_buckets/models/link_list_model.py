from .link_model import Link


class LinkList:

    def __init__(self, bucket_id):
        self.link_list = Link.query.filter_by(bucket_id=bucket_id).all()

    def append_link(self, link: Link):
        pass

    def remove_link(self, link_id: Link.id):
        pass
