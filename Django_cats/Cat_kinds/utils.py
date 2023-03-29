from Cat_kinds.models import CatKinds


def plus_like(obj=None):
    if obj is not None:
        sub = obj.likes
        obj.likes = sub + 1
        obj.save()


DB = CatKinds.objects.all()

american = DB[1]
british = DB[2]
abyss = DB[5]
bengal = DB[0]
manul = DB[3]
siamese = DB[4]