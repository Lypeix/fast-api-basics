def get_next_note_id(notes):
    existing_ids = [note["id"] for note in notes]
    return max(existing_ids, default=0) + 1