from notebook import notes_col
#just to clear my notes_col in case of testing
x = notes_col.delete_many({})

print(x.deleted_count, " documents deleted.")