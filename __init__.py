from anki.cards_pb2 import Card
from anki.notes import Note

from aqt.utils import tooltip
from aqt.operations import QueryOp
from aqt import gui_hooks, mw
from aqt.qt import *

from .promptModel import *
from .prompt import *

def generateNewCardContents(originalContent: str) -> str:
    # (My Background Operation)
    return prompt_gemini(prompt + originalContent)
def fieldNotFound():
    showInfo(
        "Phoenix Math could not find one of the required fields in your MATH note template. Please double check that your MATH note fields are correct")
    QTimer.singleShot(0, lambda: tooltip(f"Could not change card due to note formatting errors"))
    mw.undo()

def onSuccess(card_id: int, new_contents):
    # (On Success Operation)
    col = mw.col
    card = col.get_card(card_id)
    note = card.note()
    if not ("HTTP Error" in new_contents):
        try:
            note["MATH QUESTION"] = new_contents.split("question>")[1][1:-2]
            mw.col.update_note(note)
            note["MATH ANSWER"] = new_contents.split("answer>")[1][1:-2]
            mw.col.update_note(note)
            QTimer.singleShot(0, lambda: tooltip(f"Card {card_id} was changed to... {new_contents}."))
        except KeyError:
            fieldNotFound()
        except:
            QTimer.singleShot(0, lambda: tooltip(f"Could not change {card_id}. An unknown error occurred."))
            mw.undo()
    else:
        showInfo(new_contents)
        QTimer.singleShot(0, lambda: tooltip(f"Card {card_id} was not changed due to an error:"))
    if mw.state == "review":
        mw.reviewer._redraw_current_card()


def handleGivenCardReview(_, card: Card, ease) -> None:
    # (My UI Action)
    try:
        note = card.note()
        config = mw.addonManager.getConfig(__name__)
        if note.note_type()["name"] != "MATH" or not config["remix_reviewed_cards"]:
            return
        originalQuestion = note["MATH QUESTION"]
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

        QTimer.singleShot(0, lambda: tooltip(f"Formulating New Question for card {cid}..."))
        # op.run_in_background()
        op.without_collection().run_in_background()
    except KeyError:
        fieldNotFound()

def handleGivenCardAddition(note: Note):
    card = note.cards()[0]
    config = mw.addonManager.getConfig(__name__)
    if card.note_type()["name"] != "MATH":
        return
    if not config["remix_newly_added_cards"]:
        return
    try:
        originalQuestion = note["MATH QUESTION"]
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
        QTimer.singleShot(0, lambda: tooltip(f"Formulating New Question for recently added card {cid}..."))
        op.without_collection().run_in_background()
    except KeyError:
        fieldNotFound()

gui_hooks.reviewer_did_answer_card.append(handleGivenCardReview)
gui_hooks.add_cards_did_add_note.append(handleGivenCardAddition)
# TODO remix added cards, add setting for this in config

