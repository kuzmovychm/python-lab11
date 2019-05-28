from app import ma


class ToySchema(ma.Schema):
    class Meta:
        fields = ('id', 'price', 'size')

