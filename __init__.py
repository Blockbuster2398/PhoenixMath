from anki.cards_pb2 import Card

from aqt.utils import showInfo, tooltip
from aqt.operations import QueryOp
from aqt import gui_hooks, mw
from aqt.qt import *

from .promptModel import *
from .prompt import *


def generateNewCardContents(originalContent: str) -> str:
    # (My Background Operation)
    return prompt_gemini(prompt + originalContent)
def onSuccess(card_id: int, new_contents):
    # (On Success Operation)
    col = mw.col
    card = col.get_card(card_id)
    note = card.note()
    if not ("HTTP Error" in new_contents):
        note["MATH Question"] = new_contents.split("question>")[1][1:-2]
        mw.col.update_note(note)
        note["MATH Answer"] = new_contents.split("answer>")[1][1:-2]
        mw.col.update_note(note)
        QTimer.singleShot(0, lambda: tooltip(f"Card {card_id} was changed to... {new_contents}."))
    else:
        showInfo(new_contents)
        QTimer.singleShot(0, lambda: tooltip(f"Card {card_id} was not changed due to an error."))
    # TODO Refresh UI Screen

def handleGivenCard(_, card: Card, ease) -> None:
    # (My UI Action)
    if mw.state != "review":
        return
    note = card.note()
    originalQuestion = note["MATH Question"]
    # showInfo(originalQuestion)
    cid = card.id

    op = QueryOp(
        # the active window (main window in this case)
        parent=mw,
        # the operation is passed the collection for convenience; you can
        # ignore it if you wish
        op=lambda col: generateNewCardContents(originalQuestion),
        # this function will be called if op completes successfully,
        # and it is given the return value of the op
        success=lambda new_contents: onSuccess(cid, new_contents)
    )
    if card.note_type()["name"] == "MATH":
        QTimer.singleShot(0, lambda: tooltip(f"Formulating New Question for card {cid}..."))
        op.run_in_background()


gui_hooks.reviewer_did_answer_card.append(handleGivenCard)
