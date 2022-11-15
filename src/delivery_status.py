from enum import IntEnum


class delivery_status(IntEnum):
    PENDING = 1,
    PAID = 2,
    READY_FOR_DISPATCH = 3,
    DISPATCHED = 4,
    REJECTED = 5,
    DELIVERED = 6,

