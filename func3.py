def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses={'math','art'}
info={'name':'niraj','age':20}
student_info(*courses, **info)