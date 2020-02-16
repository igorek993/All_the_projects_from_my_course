# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from lesson_005.room_1 import folks
from lesson_005.room_2 import folks as folks_2

a = ','
print('В комнате room_1 живут:', a.join(folks), 'В комнате room_2 живут:', a.join(folks_2))

# Is there any other way of doing it? How would I put a dot after the first sentence for example?
