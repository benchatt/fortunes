from google.protobuf.timestamp_pb2 import Timestamp
from time import timezone

import proto.card_pb2 as card_pb2
import proto.webtime_pb2 as webtime_pb2

def get_tz_offset():
    return int(-timezone / 3600)

def card_major():
    message = card_pb2.Card(
        major=card_pb2.Card.MajorArcana.THE_HANGED_MAN,
        inverted=True
    )
    return message

def card_minor_num():
    message = card_pb2.Card(
        minor=card_pb2.Card.MinorArcana(
            suit=card_pb2.Card.Suit.SWORDS,
            number=9
        ),
        inverted=False
    )
    return message

def card_minor_face():
    message = card_pb2.Card(
        minor=card_pb2.Card.MinorArcana(
            suit=card_pb2.Card.Suit.WANDS,
            name=card_pb2.Card.NamedRank.ACE
        ),
        inverted=False
    )
    return message

def connection():
    message = card_pb2.Connection(
        label='career',
        card=card_pb2.Card(
            major=card_pb2.Card.MajorArcana.THE_TOWER,
            inverted=True
        ),
        url="https://en.wikipedia.org/wiki/The_Tower_(Tarot_card)"
    )
    return message

def spread(conn1: card_pb2.Connection):
    message = card_pb2.Spread(
        connections = [
            conn1,
            card_pb2.Connection(
                label='love',
                card=card_pb2.Card(
                    major=card_pb2.Card.MajorArcana.DEATH,
                    inverted=False
                ),
                url="https://en.wikipedia.org/wiki/Death_(Tarot_card)"
            )
        ]
    )
    return message

def webtime():
    nt = Timestamp()
    nt.GetCurrentTime()
    return webtime_pb2.Webtime(
        internetTime=webtime_pb2.Webtime.InternetTime(
            beats=113,
            ticks=13
        ),
        normalTime=nt,
        offset=get_tz_offset()
    )

if __name__ == '__main__':
    # print(card_major())
    # print(card_minor_num())
    # print(card_minor_face())
    # conn = connection()
    # print(conn)
    # print(spread(conn))
    print(webtime())