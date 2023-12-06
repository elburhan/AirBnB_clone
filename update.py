def do_update(self, arg):
    """
    Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
    Example: update BaseModel 1234-1234-1234 email "aibnb@mail.com".
    """
    args = arg.split()

    try:
        class_name, instance_id = self.split_arg(args)
    except TypeError:
        return  # Error messages are already printed in split_arg

    # Check for missing arguments
    if len(args) < 4:
        print("Please provide attribute name and value to update.")
        return
    attribute_name, attribute_value = args[2], args[3]

    # Check for valid attribute update
    if attribute_name not in ["id", "created_at", "updated_at"]:
        # Check if the provided attribute exists for the model
        valid_attributes = ["string_attribute", "integer_attribute", "float_attribute"]  # Replace with actual attribute names
        if attribute_name not in valid_attributes:
            print(f"Invalid attribute name: {attribute_name}")
            return
    else:
        print(f"Cannot update reserved attribute: {attribute_name}")
        return

    key = f"{class_name}.{instance_id}"

    instances = storage.all()

    if key in instances:
        instance = instances[key]
        # Update only simple attributes: string, integer, and float
        if isinstance(getattr(instance, attribute_name, None), (str, int, float)):
            # Cast the attribute value to the attribute type
            setattr(instance, attribute_name, type(getattr(instance, attribute_name))(attribute_value))
            instance.save()
            print(f"Attribute {attribute_name} updated to {attribute_value} for instance {instance_id} of class {class_name}.")
        else:
            print(f"Cannot update non-simple attribute: {attribute_name}")
    else:
        print("** no instance found **")

