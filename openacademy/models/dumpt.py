@api.depends('attendee_ids')
def _get_attendees_count(self):
    for r in self:
        r.attendees_count = len(r.attendee_ids)