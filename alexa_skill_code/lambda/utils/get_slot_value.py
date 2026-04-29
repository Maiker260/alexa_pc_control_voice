def get_slot_value(slots, name):
    if not slots:
        return None
    slot = slots.get(name)
    return slot.value if slot else None