collected_items = input().split(", ")

command = input()

while command != "Craft!":
    new_items, item_for_collected = command.split(' - ')

    if new_items == "Collect":
        if item_for_collected not in collected_items:
            collected_items.append(item_for_collected)

    elif new_items == "Drop":
        if item_for_collected in collected_items:
            collected_items.remove(item_for_collected)

    elif new_items == "Combine Items":
        old_item,new_item = item_for_collected.split(":")
        if old_item in collected_items:
            old_index = collected_items.index(old_item)
            collected_items.insert(old_index+1,new_item)

    elif new_items == "Renew":
        if item_for_collected in collected_items:
            collected_items.pop(collected_items.index(item_for_collected))
            collected_items.append(item_for_collected)
    command = input()

print(", ".join(collected_items))
