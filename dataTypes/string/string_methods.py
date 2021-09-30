# string methods
name = 'java'
course = f"{name} programming language"
# course = 'PYTHON'

print(course.upper())
print(course.lower())
print(course.capitalize())
print(course.title())
print(course.strip())
print(course.lstrip())
print(course.rstrip())
print(course.replace("p", "j"))

print(course.find("Pro"))
print(course.find("pro"))
print(course.split())

print(course.format(name,))
# del course

print(course)
