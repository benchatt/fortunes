from google.protobuf.timestamp_pb2 import Timestamp
from time import timezone

import proto.card_pb2 as card_pb2
import proto.webtime_pb2 as webtime_pb2
import proto.emojimancy_pb2 as emojimancy_pb2
import proto.yijing_pb2 as yijing_pb2
import proto.season_pb2 as season_pb2
import proto.strategy_pb2 as strategy_pb2
import proto.writingprompt_pb2 as writingprompt_pb2
import proto.magicword_pb2 as magicword_pb2

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

def emojis():
    return emojimancy_pb2.EmojiCard(
        set_1=emojimancy_pb2.EmojiCard.EmojiSet(
            emoji_1='⚧',
            emoji_2='🚩',
            emoji_3='🖊',
            label='the nature of the problem'
        ),
        set_2=emojimancy_pb2.EmojiCard.EmojiSet(
            emoji_1='🦮',
            emoji_2='🖖',
            emoji_3='🌂',
            label='the nature of the solution'
        ),
        set_3=emojimancy_pb2.EmojiCard.EmojiSet(
            emoji_1='🔔',
            emoji_2='🎺',
            emoji_3='🍖',
            label='a word of warning'
        )
    )

def yijing():
    return yijing_pb2.YijingDraw(
        yijing=yijing_pb2.YijingDraw.Yijing(
            hexagram='䷂',
            hanzi='屯',
            title='Beginning'
        ),
        opposite=yijing_pb2.YijingDraw.Yijing(
            hexagram='䷱',
            hanzi='鼎',
            title='Establishing the New'
        ),
        description="Difficulty at the Beginning works supreme success,\nFurthering through perseverance.\nNothing should be undertaken.\nIt furthers one to appoint helpers."
    )

def magicword():
    return(
        magicword_pb2.MagicWord(
            word='bird'
        ),
        magicword_pb2.MagicWord(
            empty=True
        )
    )

def strategy():
    return(strategy_pb2.Strategy(strategy="Don't Panic"))

def writingprompt():
    return(
        writingprompt_pb2.WritingPrompt(
            character='orphaned farmboy',
            premise='joins the resistance against an evil empire',
            turn="and must learn the truth about his late father's legacy"
        )
    )

def season():
    return season_pb2.Season(
        moonPhase=season_pb2.Season.MoonPhaseResult(
            last=season_pb2.Season.MoonPhase.FULL,
            next=season_pb2.Season.MoonPhase.LAST_QUARTER,
            daysSinceLast = 6,
            daysUntilNext = 1
        ),
        stationDays=season_pb2.Season.StationDaysResult(
            last=season_pb2.Season.StationDays.AUGUST_CROSS_QUARTER,
            next=season_pb2.Season.StationDays.SEPTEMBER_EQUINOX,
            daysSinceLast = 10,
            daysUntilNext = 36
        )
    )

if __name__ == '__main__':
    # print(card_major())
    # print(card_minor_num())
    # print(card_minor_face())
    # conn = connection()
    # print(conn)
    # print(spread(conn))
    # print(webtime())
    # print(emojis())
    # print(yijing())
    # print(magicword())
    # print(strategy())
    # print(writingprompt())
    print(season())