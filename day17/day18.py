#  Code to Enforce Class Naming Convention with a Metaclass
class NamingConventionMeta(type):
    def __new__(cls, name, bases, class_dict):
        if not name[0].isupper() or '_' in name:
            raise TypeError(f"Class name '{name}' must begin with an uppercase and no underscore.")
        return type.__new__(cls, name, bases, class_dict)

# Incorrect usage
class incorrect_naming_convention(metaclass=NamingConventionMeta):
    pass

# Correct usage
class CorrectNamingConvention(metaclass=NamingConventionMeta):
    pass