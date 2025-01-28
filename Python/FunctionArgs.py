def Dict_Call(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"items in args are: {args}")
    print(f"items in args are: {type(args)}")
    print(f"Total number of items: {len(args)}")
    print(f"items in args are: {kwargs}")
    return kwargs

result = Dict_Call(
    "Sai", 1.5, 2.7, 3, 4, 50, DOB="09-01-1999", BirthPlace="Guntur"
)

print("Returned dictionary:", result)
