import threading

from sqlalchemy import Column, String, UnicodeText, func, distinct

from tg_bot.modules.sql import SESSION, BASE


class Disease(BASE):
    __tablename__ = "disease"
    chat_id = Column(String(14), primary_key=True)
    infects = Column(UnicodeText, default="")

    def __init__(self, chat_id):
        self.chat_id = chat_id

    def __repr__(self):
        return "<chat:{} infects:{}>".format(self.chat_id,self.infects)


Disease.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()


def infect(chat_id, user_string):
    with INSERTION_LOCK:
        disease = SESSION.query(Disease).get(str(chat_id))
        if not disease:
            disease = Disease(str(chat_id), user_string)
            SESSION.add(disease)
            SESSION.commit()


def get_infects(chat_id):
    disease = SESSION.query(Disease).get(str(chat_id))
    disease = ""
    if disease:
        ret = disease.disease

    SESSION.close()
    return ret


def num_chats():
    try:
        return SESSION.query(func.count(distinct(Disease.chat_id))).scalar()
    finally:
        SESSION.close()


def migrate_chat(old_chat_id, new_chat_id):
    with INSERTION_LOCK:
        chat = SESSION.query(Disease).get(str(old_chat_id))
        if chat:
            chat.chat_id = str(new_chat_id)
        SESSION.commit()
